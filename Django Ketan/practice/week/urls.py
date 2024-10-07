from django.urls import path
from .import views

urlpatterns = [
    path('<int:week>',views.weekly_task_by_number),
    path('<str:week>',views.weekly_task,name='week-name'),
  
]