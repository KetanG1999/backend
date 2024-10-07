from django.urls import path
from .import views
urlpatterns = [
    path('<int:month>',views.monthly_task_by_number),
    path('<str:month>',views.monthly_task,name='month-name'),
]

#<angle bracket>---> as a placeholder
# str, int.....
#part of the url to be captuured enclosing the na,me of the  varible thet the view
#can use the access the capturred data.