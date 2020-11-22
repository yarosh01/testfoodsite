from django.urls import path
from . import views
from .views import Index, contact_view, success_view, UserProfileListCreateView, userProfileDetailView

urlpatterns = [
    path('', Index.as_view(), name='index'),
    # path('reserv', views.get_query, name='reserv'),
    path('reserv/', contact_view, name='reserv'),
    path('success/', success_view, name='success'),
    #gets all user profiles and create a new profile
    path("all-profiles", UserProfileListCreateView.as_view(),name="all-profiles"),
   # retrieves profile details of the currently logged in user
    path("profile/<int:pk>",userProfileDetailView.as_view(),name="profile"),
]
