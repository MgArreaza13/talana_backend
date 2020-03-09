from django.contrib import admin
from django.urls import path, re_path, include
from apps.accounts import views

urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('create/', views.ManagementUserViewSet.as_view(), name='new_user'),
]