from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'teacher_create_task',views.teacher_create_task_viewset, basename='teacher_create_task')
router.register(r'student_view_task',views.student_view_task_viewset, basename='student_view_task')
router.register(r'student_submit_task',views.student_submit_task_viewset,basename='student_submit_task')
router.register(r'teacher_get_task',views.teacher_viewset,basename='teacher_get_task')
router.register(r'teacher_accept_task',views.teacher_task_accept_viewset,basename='teacher_accept_task')
router.register(r'pagenation',views.pagenation_viewset,basename='pagenation')


urlpatterns = [
    path('', include(router.urls)),

    
]