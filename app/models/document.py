from django.db import models

from app.models.organization import Organization


class Document(models.Model):
    organization_id = models.IntegerField(null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    from_whom = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, related_name='from_whom')
    to_whom = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, related_name='to_whom')