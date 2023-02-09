from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name="home"),
    path('', views.test_path, name="test_path"),
    path('test_path/', views.test_path, name="test_path")
]