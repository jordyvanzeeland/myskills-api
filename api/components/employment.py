from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Employment as EmploymentModel
from ..serializers import EmploymentSerializer

class Employment(APIView):
    def getEmployment(self, pk):
        try:
            return EmploymentModel.objects.get(pk=pk)
        except EmploymentModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None):
        if pk:
            employment = self.getEmployment(pk)
            serializer = EmploymentSerializer(employment)
            return Response(serializer.data)
        
        employment = EmploymentModel.objects.get()
        serializer = EmploymentSerializer(employment)
        return Response(serializer.data)

    def post(self, request):
        serializer = EmploymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        employment = self.getEmployment(pk)
        serializer = EmploymentSerializer(employment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        employment = self.getEmployment(pk)
        employment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)