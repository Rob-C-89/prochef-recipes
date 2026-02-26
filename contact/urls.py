from . import views
from django.urls import path

urlpatterns = [
    path('contact_us/', views.contact_us, name='contact_us'),
]