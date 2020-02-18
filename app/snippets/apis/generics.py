from rest_framework import generics, permissions

from ..models import Snippets
from ..serializer import SnippetSerializer, SnippetCreateSerializer


class SnippetListCreateAPIView(generics.ListCreateAPIView):
    queryset = Snippets.objects.all()
    # 인증된 사용자가 아니라면, list, retrieve 요청만 가능
    # create, update, destroy요청은 인증된 사용자만 가능
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )

    def get_serializer_class(self):
        # 요청 메서드에 따라 사용하는 Serializer Class를 구분
        if self.request.method == 'GET':
            return SnippetSerializer
        elif self.request.method == 'POST':
            return SnippetCreateSerializer

    def perform_create(self, serializer):
        # Serializer를 통해 모델 인스턴스가 생성되는 순간 author필드값을 채워 줌
        serializer.save(author=self.request.user)


class SnippetRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippets.objects.all()
    serializer_class = SnippetSerializer
