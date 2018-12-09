from django.urls import path
from . import views

urlpatterns = [
    path('sbl/', views.upload_file, name='home'),
]