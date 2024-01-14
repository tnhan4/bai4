from . import views
from django.urls import path
urlpatterns = [
    path("hello/", views.hello),
    path("vaotrangchu/", views.home),
    path('user', views.demo, name = 'demo'),
    path('home', views.home, name = 'home'),
    path('product', views.product, name='product'),
    path('show', views.show, name = 'show')
]