from django.contrib import admin
from .models import Teacher
# Register your models here.
@admin.register(Teacher)
class UserAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','department']
    list_filter=['is_active','create_at','update_at']
    search_fields=['name','email','phone']
