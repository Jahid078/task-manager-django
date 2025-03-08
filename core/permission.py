
from rest_framework.permissions import BasePermission
from rest_framework.exceptions import AuthenticationFailed
import jwt
from simple_setup import settings
from rest_framework.response import Response
from rest_framework import status
from student.models import Student


class IsStudentAuthentication(BasePermission):
    def has_permission(self, request, view):
        SECRET_KEY = settings.SECRET_KEY 
        if("App-AUTH" in request.headers):
            auth_header = request.headers["App-AUTH"]
            if('Bearer' in auth_header):
                j_token= str(auth_header).replace("Bearer ", "").strip()
                decode = jwt.decode(j_token,settings.SECRET_KEY, algorithms=["HS256"])
                request.user_id=decode['id']
                return decode
            
class IsTeacherAuthentication(BasePermission):
    def has_permission(self, request, view):
        SECRET_KEY = settings.SECRET_KEY 
        if("App-AUTH" in request.headers):
            auth_header = request.headers["App-AUTH"]
            if('Bearer' in auth_header):
                j_token= str(auth_header).replace("Bearer ", "").strip()
                decode = jwt.decode(j_token,settings.SECRET_KEY, algorithms=["HS256"])
                request.user_id=decode['id']
                return decode
            
  