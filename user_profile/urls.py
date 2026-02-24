from django.urls import path
from . import views

urlpatterns = [
    path('my_profile/', views.my_profile, name='my_profile'),
    path('create_profile/', views.create_profile, name='create_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('delete_profile/', views.delete_profile, name='delete_profile'),
    path('profile/<str:username>/', views.view_profile, name='view_profile'),
]
