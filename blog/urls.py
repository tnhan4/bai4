from . import views
from django.urls import path
urlpatterns = [
    # path("hello/", views.hello, name="home"),
    path("trangchu", views.home, name="trangchu"),
    path('product-detail/<int:pk>', views.product_detail, name="product-detail"),
]