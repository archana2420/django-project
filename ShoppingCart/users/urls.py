from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    
    path('register',RegisterUserAPI.as_view(),name="user_registration"),
    path('list-all',ListAllUsersAPI.as_view(),name='list_users'),
    path('update-user/<int:pk>',UpdateUserAPI.as_view(),name='update_user'),
    path('delete-user/<int:pk>',DeleteUserAPI.as_view(),name='delete_user'),
    

]