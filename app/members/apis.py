from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import UserSerializer


class AuthTokenAPIView(APIView):
    def post(self, request):
        # url: /members/auth-token/
        #   members.urls를 사용
        #   config.urls에서는 include
        # Postman에서 작동되는지 확인

        # Hint
        #  request.data로 전달된 내용을 적절히 사용
        #   (Serializer는 사용하지 않음)

        # 1. url과 이 view를 연결, Postman에 작성
        # 2. Postman의 body에 작성한 내용이
        #    Send버튼을 누른 뒤 이 view의
        #    request.data에 원하는 데이터가 오고 있는지 확인
        # 3. 적절한 데이터가 온다면 그 때 authenticate()함수를 사용,
        #    User객체를 얻어냄
        username = request.data['username']
        password = request.data['password']
        user = authenticate(username=username, password=password)

        # 4. 얻어낸 User객체와 연결되는 Token을 get_or_create()로
        #    가져오거나 생성
        if user:
            token, _ = Token.objects.get_or_create(user=user)
        else:
            raise AuthenticationFailed()

        # 5. 생성된 Token의 'key'속성을 적절히 반환
        data = {
            'token': token.key,
            'user': UserSerializer(user).data,
        }
        return Response(data)
