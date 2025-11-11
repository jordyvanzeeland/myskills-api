from django.contrib.auth import authenticate, get_user_model
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import jwt
from datetime import datetime, timedelta

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({'error': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

    payload = {
        'id': user.id,
        'name': f'{user.first_name} {user.last_name}'.strip(),
        'username': user.username,
        'email': user.email,
        'exp': datetime.utcnow() + timedelta(hours=1), 
        'iat': datetime.utcnow(),
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

    return Response({
        'user': {
            'id': user.id,
            'name': payload['name'],
            'username': user.username,
            'email': user.email
        },
        'token': token
    }, status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    User = get_user_model()

    email = request.data.get('email')
    username = request.data.get('username')
    password = request.data.get('password')

    if not email or not username or not password:
        return Response({'error': 'Email, username, and password are required.'},status=status.HTTP_400_BAD_REQUEST)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists.'}, status=status.HTTP_400_BAD_REQUEST)
    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email already registered.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user = User.objects.create_user(username=username, email=email, password=password)
        return Response({'message': 'User registered successfully.'},status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'error': f'Error creating user: {str(e)}'},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
