from django.urls import path

from app.api.organization import views

urlpatterns = [
    path('create', views.OrganizationCreateAPIView.as_view(), name='organization_create_api'),
]