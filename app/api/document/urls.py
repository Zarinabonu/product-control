from django.urls import path

from app.api.document import views

urlpatterns = [
    path('create', views.DocumentCreateAPIView.as_view(), name='document_create_api'),
]