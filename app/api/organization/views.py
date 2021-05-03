from rest_framework.generics import CreateAPIView

from app.api.organization.serializers import OrganizationSerializer
from app.models import Organization


class OrganizationCreateAPIView(CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
