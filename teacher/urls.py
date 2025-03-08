from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router=DefaultRouter()
router.register(r'register',views.register_viewset,basename='register')
router.register(r'login',views.login_viewset,basename='login')
router.register(r'get',views.get_viewset,basename='get')
router.register(r'update',views.update_viewset,basename='update')
router.register(r'delete',views.delete_viewset,basename='delete')
router.register(r'password_change',views.change_password_viewset,basename='password_change')



urlpatterns = [
    path('', include(router.urls)),
    
]