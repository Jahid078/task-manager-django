from django.db import models
# Create your models here.
class common(models.Model):
    is_active=models.BooleanField(default=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now_add=True)
    
class Teacher(common):
    name=models.CharField(max_length=30,null=True,blank=True)
    password=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    phone = models.CharField(max_length=10,null=True,blank=True)
    address=models.CharField(max_length=30,null=True,blank=True)
    department=models.CharField(max_length=30,null=True,blank=True)
    
    def __str__(self):
        return f"{self.email}"
