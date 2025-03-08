from rest_framework import serializers
from .models import Task



class TeacherCreateTaskSerializer(serializers.ModelSerializer):
    is_active = serializers.BooleanField(default=True)
    class Meta:
        model = Task
        fields =  ['title','status','description','student_task','is_active','due_date','id']


    def create(self, validated_data):
        id=self.context.get('id')
        validated_data['teacher_task_id'] = id
        
        task = Task.objects.create(**validated_data)
        return task
    

class StudentViewTaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['title', 'description', 'status','teacher_task','due_date']


class StudentsubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=['status']


class TeacherTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'


class TacherTaskAcceptSerializer(serializers.ModelSerializer):
    class Meta:
        model=Task
        fields=['status']
    
