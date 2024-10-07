from django.urls import path
from .import views
urlpatterns = [
    # path('<int:seasonname>',views.Season_int_url),
    path('<str:seasonname>',views.Season_str_url)
]
