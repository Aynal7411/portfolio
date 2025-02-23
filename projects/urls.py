from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_projects, name='my_projects'),
    path('<int:project_id>/', views.project_detail_page, name='project_detail'),
   
]
