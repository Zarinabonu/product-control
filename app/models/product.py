from django.db import models

from app.models.document import Document


class Product(models.Model):
    document = models.ForeignKey(Document, on_delete=models.SET_NULL, null=True)
    name = models.TextField(null=True, blank=True)
    measurement = models.TextField(null=True, blank=True)
    quantity = models.IntegerField(null=True, blank=True)
    sum = models.FloatField(null=True, blank=True)