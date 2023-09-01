from django.urls import path
from .views import CustomUserCreate, HealthCheck

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreate.as_view(), name="create_user"),
    path('health-check/', HealthCheck.as_view(), name="health_check"),
]