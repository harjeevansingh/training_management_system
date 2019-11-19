from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='student_dashboard'),
    path('add_training/', views.add_training, name='add_training'),
    path('add_project/', views.add_project, name='add_project'),
    path('all_projects/', views.all_projects, name='all_projects'),


]
