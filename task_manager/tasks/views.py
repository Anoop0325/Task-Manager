# views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authentication import TokenAuthentication
from .models import Task, User
from .serializers import TaskSerializer

class TaskCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TaskAssignView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, id):
        try:
            task = Task.objects.get(id=id)
        except Task.DoesNotExist:
            return Response(
                {"error": "Task not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        user_ids = request.data.get('user_ids', [])
        users = User.objects.filter(id__in=user_ids)
        task.assigned_users.set(users)
        
        serializer = TaskSerializer(task)
        return Response(serializer.data)

class UserTasksView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user_id = request.GET.get("id")
        if not user_id:
            return Response(
                {"error": "User ID is required as a query parameter (?id=)"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if user_id:
            task = Task.objects.filter(assigned_users = user_id).values()
            return Response({"tasks": list(task)})