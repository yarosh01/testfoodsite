from django.urls import path
from . import views
from .views import Index, contact_view, success_view

urlpatterns = [
    path('', Index.as_view(), name='index'),
    # path('reserv', views.get_query, name='reserv'),
    path('reserv/', contact_view, name='reserv'),
    path('success/', success_view, name='success'),

]
