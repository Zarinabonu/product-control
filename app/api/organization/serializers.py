from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from app.models import Organization


class OrganizationSerializer(ModelSerializer):
    class Meta:
        model = Organization
        fields = ('__all__')

    def create(self, validated_data):
        org = Organization(**validated_data)
        user = User.objects.create(username=org.name)
        user.set_password(org.password)
        user.save()
        return org