from django.contrib import admin

from app.models import Document, Organization, Product

admin.site.register(Document)
admin.site.register(Organization)
admin.site.register(Product)

# Register your models here.
