
from django.shortcuts import render
import uuid
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializer import UserSerializer,LoginSerializer,GetSerializer,UpdateSerializer,DeleteSerializer,ChangePasswordSerializer
from .models import Student
from core.permission import IsStudentAuthentication
import jwt
from simple_setup import settings
from rest_framework import viewsets  
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse



class register_viewset(ModelViewSet):
    http_method_name=['post']
    queryset=Student.objects.all()
    serializer_class=UserSerializer
    

class login_viewset(ModelViewSet):
    http_method_names=['post']
    queryset=Student.objects.all()
    serializer_class=LoginSerializer

    def create(self, request):
        email = request.data.get("email")
        SECRET_KEY = settings.SECRET_KEY 
        if not email:
           return Response({"error": "Email  are required"}, status=400)
        user= Student.objects.filter(email=email).first()
        if user:
            user_id = user.id
        else:
            return Response({'error': "Email not valid"})
        encoded_jwt = jwt.encode({'id':user_id, 'secret_token':str(uuid.uuid4())}, SECRET_KEY, algorithm='HS256')

        return Response({
            'token': encoded_jwt
        })

class get_viewset(ModelViewSet):
    permission_classes = [IsStudentAuthentication]
    http_method_names=['get']
    serializer_class=GetSerializer


    def get_queryset(self):
        teacher_id=self.request.user_id
        return Student.objects.filter(id=teacher_id)
    

class update_viewset(ModelViewSet):
    permission_classes=[IsStudentAuthentication]
    http_method_names=['patch']
    serializer_class=UpdateSerializer

    def partial_update(self, request, *args, **kwargs):
        id=self.request.user_id
        requested_id = kwargs.get('pk')  
        if int(requested_id) !=id:
            return Response({'error': 'You can only update your own profile'}, status=403)

        
        user = Student.objects.filter(id=id).first()

        if not user:
            return Response({'error': 'User not found'}, status=404)

        serializer = self.get_serializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User updated successfully', 'updated_data': serializer.data})
        
    
class delete_viewset(ModelViewSet):
    http_method_names=['delete']
    permission_classes=[IsStudentAuthentication]
    serializer_class=DeleteSerializer


    def get_queryset(self):
        return Student.objects.filter(id=self.request.user_id)
    

class change_password_viewset(ModelViewSet):
    permission_classes=[IsStudentAuthentication]
    http_method_names=['patch']
    serializer_class=ChangePasswordSerializer


    def partial_update(self, request, *args, **kwargs):
        teacher_id=self.request.user_id
        teacher=Student.objects.filter(id=teacher_id).first()
        if not teacher:
            return Response({'error':'teacher not found'})
        
        password=teacher.password
        print(password,'ppp')
        current_password=request.data.get('current_password')
        new_password=request.data.get('new_password')

        if not current_password or not new_password:
            return Response({'error':'Both current_password and new_password requred'})
        
        if check_password(current_password,teacher.password):
            teacher.password=make_password(new_password)
            teacher.save()
            return Response({'Password Update successfully'})
        else:
            return Response({'Incorrect Password'})