from django.urls import path, include

from app import views

urlpatterns = [
    path('api/', include('app.api.urls')),
    path('login', views.Login.as_view(), name='login'),
    path('org/list', views.OrganizationList.as_view(), name='org_list'),
    path('doc/list', views.DocumentList.as_view(), name='doc_list'),
]
