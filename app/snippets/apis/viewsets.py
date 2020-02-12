from rest_framework import viewsets

from ..models import Snippets
from ..serializer import SnippetSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer
