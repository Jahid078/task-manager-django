from django.contrib import admin
from .models import Task


# Register your models here.
@admin.register(Task)
class AdminUser(admin.ModelAdmin):
    list_display=['title','description','status']
    search_fields=['title','status','due_date']
    


