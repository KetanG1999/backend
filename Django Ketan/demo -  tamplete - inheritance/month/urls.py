from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:month>',views.monthly_task_by_number),
    path('<str:month>',views.monthly_task,name='month-name'), #month/

]
#<angle bracket> --> as a placeholder
#part of the URL to be captured , enclosing the name
#of the variable that the view can use to access the
#captured data
#< month > --> variable
#str,int....