from django.contrib import admin
from .models import Student
# Register your models here.



@admin.register(Student)
class UserAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','branch']
    search_fields=['name','email','phone']
    list_filter=['create_at','update_at']
