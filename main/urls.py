from django.urls import path
from .views import Index, contact_view, success_view, RegisterAPI

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('reserv/', contact_view, name='reserv'),
    path('success/', success_view, name='success'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
]
