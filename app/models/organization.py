from django.db import models


class Organization(models.Model):
    name = models.TextField(null=True, blank=True)
    password = models.TextField(blank=True, null=True)
    address = models.TextField(null=True, blank=True)