from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.custom_login, name='login'),
    path('upload/', views.upload_file, name='upload'),
    path('files/', views.file_list, name='file_list'),
    path('download/<int:file_id>/', views.download_file, name='download'),
]
