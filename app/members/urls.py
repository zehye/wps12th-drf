from django.urls import path

from . import apis

app_name = 'members'
urlpatterns = [
    path('auth-token/', apis.AuthTokenAPIView.as_view()),
]