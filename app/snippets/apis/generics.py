from rest_framework import generics

from ..models import Snippets
from ..serializer import SnippetSerializer


class SnippetListCreateAPIView(generics.ListCreateAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer


class SnippetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer
