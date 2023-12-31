from . import views
from django.urls import path
urlpatterns = [
    path("hello/", views.hello),
    path("vaotrangchu/", views.home)
]