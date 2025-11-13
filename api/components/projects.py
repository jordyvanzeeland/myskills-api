from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..models import Projects as ProjectModel
from ..serializers import ProjectSerializer

class Projects(APIView):
    def getProject(self, pk):
        try:
            return ProjectModel.objects.get(pk=pk)
        except ProjectModel.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk=None):
        if pk:
            project = self.getProject(pk)
            serializer = ProjectSerializer(project)
            return Response(serializer.data)
        
        project = ProjectModel.objects.get()
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        project = self.getProject(pk)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        project = self.getProject(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)