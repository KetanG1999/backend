from django.urls import path
from .import views
urlpatterns = [
    path('jan',views.jan),
    path('feb',views.feb),
    path('march',views.march),
    path('april',views.april),
    path('may',views.may),
]