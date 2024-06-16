from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
urlpatterns = [
    # path("hello/", views.hello, name="home"),
    re_path(r'^.*$', views.err_404_not_found),
    path("trangchu", views.home, name="trangchu"),
    path('product-detail/<int:pk>', views.product_detail, name="product-detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
