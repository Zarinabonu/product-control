from django.urls import path

from app.api.product import views

urlpatterns = [
    path('create', views.ProductCreateAPIView.as_view(), name='product_create_api'),
]