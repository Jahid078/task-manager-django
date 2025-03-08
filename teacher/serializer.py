from rest_framework import serializers
from .models import Teacher
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from simple_setup import settings


class UserSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)
    class Meta:
        model = Teacher
        fields = ['email','password','is_active']


    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        validated_data['is_active'] = True  
        user = Teacher.objects.create(**validated_data)
        subject = 'Welcome to Our Site'
        message = f"Dear User,\n\nThank you for registering with us!."
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [user.email]

        try:
            send_mail(subject, message, from_email, recipient_list)
        except Exception as e:
            raise serializers.ValidationError({'error': f"Failed to send email: {str(e)}"})

        return user
    
    
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=['email','password']


class GetSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields='__all__'


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=['name','phone','department','address']
    
class DeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields='__all__'


class ChangePasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=['password']