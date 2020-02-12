import random

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Snippets
from .serializer import SnippetSerializer


class SnippetTest(APITestCase):
    """
    postman이 해는일을 코드로 자동화
    DB는 분리됨
    """

    def test_snippet_list(self):
        url = '/api-view/snippets/'
        response = self.client.get(url)  # http요청을 보낼 수 있음(self.client) > request와 같은 역할

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)

        for i in range(4):
            Snippets.objects.create(code='1')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

        for snippet_data in response.data:
            self.assertIn("title", snippet_data)
            self.assertIn("code", snippet_data)
            # self.assertIn("wps", snippet_data)

            self.assertEqual("1", snippet_data['code'])

            # 전달된 Snippet object(dict)의 'pk'에 해당하는 실제 Snippet model instance를
            # SnippetSerializer를 통해 serializer의 결과 snippet_data와 같은 지 비교
            pk = snippet_data['pk']
            snippet = Snippets.objects.get(pk=pk)
            self.assertEqual(
                SnippetSerializer(snippet).data,
                snippet_data
            )

    def test_snippet_create(self):
        """
        Snippet 객체를 만든다.
        """
        url = '/api-view/snippets/'
        # Snippet에 객체를 만들기 위해 클라이언트로부터 전달될 JSON객체를 Parse한 Python 객체
        data = {
            "code": 1,
        }
        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        pk = response.data['pk']
        snippet = Snippets.objects.get(pk=pk)

        # 응답에 돌아온 객체가 SnippetSerializer로 실제 Model instance를 serializer한 결과와 같은지 확인
        self.assertEqual(
            response.data,
            SnippetSerializer(snippet).data,
        )
        # 객체를 하나 생성했으니, Snippet 객체의 개수가 1개인지 확인(ORM)
        self.assertEqual(Snippets.objects.count(), 1)

    def test_snippet_delete(self):
        # 미리 객체를 5개 만들어놓는다
        # delete API를 적절히 실행 한 후, 객체가 4개가 되었는지 확인
        # 지운 객체가 실제로 존재하지 않는지 확인
        snippets = [Snippets.objects.create(code='1') for i in range(5)]
        self.assertEqual(Snippets.objects.count(),5)

        snippet = random.choice(snippets)
        url = f'/api-view/snippets/{snippet.pk}/'
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Snippets.objects.count(), 4)
        self.assertFalse(Snippets.objects.filter(pk=snippet.pk).exists())
