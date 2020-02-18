from django.test import TestCase
from model_bakery import baker
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User
from .serializer import UserSerializer


class AuthAPITest(APITestCase):
    def test_token_api(self):
        url = '/members/auth-token/'
        username = 'test_username'
        password = 'test_password'

        # 유저생성
        user = baker.make(User, username=username)
        user.set_password(password)
        user.save()

        # 전송되어 올 것이라 계획한 데이터
        data = {
            'username': username,
            'password': password,
        }

        # POST 형식으로 요청을 보내봄
        response = self.client.post(url, data)

        # 상태코드가 왔는지
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # 토큰이 왔는지 > 정상 토큰이 왔는지?
        self.assertIn('token', response.data)
        self.assertIn('user', response.data)

        # 유저 인스턴스를 serializer한 결과가 response.data와 'user'key의 value(object)와 같은지 확인
        self.assertEqual(
            UserSerializer(user).data,
            response.data['user']
        )

        # response.data의 token key의 value가 user의 전달된 token의 key인지 확인
        self.assertIsNotNone(user.auth_token)
        self.assertEqual(
            user.auth_token.key,
            response.data['token']
        )
