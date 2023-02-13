from django.urls import path,include
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    
    path('',RegisterUserAPI.as_view(),name="user_registration"),
    path('user/list-all',ListAllUsersAPI.as_view(),name='list_users'),
    path('user/update-user/<int:pk>',UpdateUserAPI.as_view(),name='update_user'),
    path('user/delete-user/<int:pk>',DeleteUserAPI.as_view(),name='delete_user'),
    

]