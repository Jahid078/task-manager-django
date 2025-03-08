from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializer import TeacherCreateTaskSerializer,StudentViewTaskSerializer,StudentsubmitSerializer,TeacherTaskSerializer,TacherTaskAcceptSerializer
from .models import Task
from core.permission import IsTeacherAuthentication,IsStudentAuthentication
from rest_framework.pagination import PageNumberPagination


class teacher_create_task_viewset(ModelViewSet):
    http_method_names=['post']
    serializer_class=TeacherCreateTaskSerializer
    permission_classes = [IsTeacherAuthentication]
    

    def get_serializer_context(self):
        id=self.request.user_id
        return {'id':id}


class student_view_task_viewset(ModelViewSet):
    http_method_names=['get']
    serializer_class=StudentViewTaskSerializer
    permission_classes = [IsStudentAuthentication]


    def get_queryset(self):
        student_id=self.request.user_id
        return Task.objects.filter(student_task_id=student_id)
    

class student_submit_task_viewset(ModelViewSet):
    http_method_names=['patch']
    serializer_class=StudentsubmitSerializer
    permission_classes=[IsStudentAuthentication]
    

    def partial_update(self, request, *args, **kwargs):
        student_id = self.request.user_id 
        task_create_id = kwargs.get('pk')  
        task = Task.objects.filter(id=task_create_id, student_task_id=student_id).first()  
        if not task:
            return Response({'error': 'Task not found or not owned by user'}, status=403)
        serializer = self.get_serializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)
        return Response(serializer.errors, status=400)
    

class teacher_viewset(ModelViewSet):
    http_method_names=['get']
    serializer_class=TeacherTaskSerializer
    permission_classes=[IsTeacherAuthentication]


    def get_queryset(self):
        teacher_id=self.request.user_id
        return Task.objects.filter(teacher_task_id=teacher_id)
    
    
class teacher_task_accept_viewset(ModelViewSet):
    http_method_names=['patch']
    serializer_class=TacherTaskAcceptSerializer
    permission_classes=[IsTeacherAuthentication]


    def partial_update(self, request, *args, **kwargs):
        teacher_id = self.request.user_id 
        task_create_id = kwargs.get('pk')  
        task = Task.objects.filter(id=task_create_id, teacher_task_id=teacher_id).first() 
        if not task:
            return Response({'error': 'Task not found or not owned by user'}, status=403)
        serializer = self.get_serializer(task, data=request.data, partial=True)

        
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data)

        return Response(serializer.errors, status=400)

  
class StudentPagination(PageNumberPagination):
    page_size = 3  

class pagenation_viewset(ModelViewSet):
    serializer_class = TeacherTaskSerializer
    queryset = Task.objects.all()
    http_method_names = ['get']
    pagination_class = StudentPagination  