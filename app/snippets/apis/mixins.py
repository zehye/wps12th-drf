from rest_framework import mixins
from rest_framework import generics
from rest_framework.response import Response

from ..models import Snippets
from ..serializer import SnippetSerializer


class SnippetListCreateAPIView(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer

    # def get(self, *args, **kwargs):
    #     objects = self.queryset
    #     serializer = self.serializer_class(objects, many=True)
    #     return Response(serializer.data)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SnippetRetrieveUpdateDestroyAPIView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                                          mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
