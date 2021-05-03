from django.urls import path, include

urlpatterns = [
    path('organization/', include('app.api.organization.urls')),
    path('document/', include('app.api.document.urls')),
    path('product/', include('app.api.product.urls'))
]