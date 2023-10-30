from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.login, name="login"),
    path('register/', views.register, name="register"),
    path('logout/', views.logout, name="logout"),
    path('api/users', views.api_user, name="api_users"),
    path('api/users/<int:id>', views.api_user_single, name="api_user_single")
    
]
