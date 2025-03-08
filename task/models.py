from django.db import models
from student.models import Student
from teacher.models import Teacher


PENDING='P'
CANCEL='C'
APPROVED='A'
COMPLETED='CD'
STATUS = (
    (PENDING,'Pending'),
    (CANCEL,'Cancel'),
    (APPROVED,'Approved'),
    (COMPLETED,'Completed')
)
PRIORITY_CHOICES = (
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    
)
class common(models.Model):
    is_active=models.BooleanField(default=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)

class Task(common):
    student_task=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='student_task')
    teacher_task=models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='teacher_task')
    title=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    status=models.CharField(max_length=10,choices=STATUS,default='P')
    due_date = models.DateField()
    priority_choices=models.CharField(max_length=10,choices=PRIORITY_CHOICES,default='medium')


    def __str__(self):
        return f"({self.title})"
