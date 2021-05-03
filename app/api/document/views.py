from rest_framework.generics import CreateAPIView

from app.api.document.serializers import DocumentSerializer
from app.models import Document


class DocumentCreateAPIView(CreateAPIView):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer