from django.contrib import admin
from django.urls import path, re_path, include
from apps.pet import views

urlpatterns = [
    path('list/', views.PetsView.as_view(), name='list_pets'),
    path('new/', views.PetOptionsView.as_view(), name='new_pets'),
    path('detail/<int:id_pet>/', views.PetOptionsView.as_view(), name='detail_pet'),
    path('edit/<int:id_pet>/', views.PetOptionsView.as_view(), name='update_pet'),
    path('delete/<int:id_pet>/', views.PetOptionsView.as_view(), name='delete_pet'),
    path('update-like/<int:id_pet>/', views.ManageViewsPetsView.as_view(), name='like_pet'),
    
]
