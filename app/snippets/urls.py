from django.urls import path
from .views import snippet_list, snippet_detail

from . import apis

app_name = 'snippets'
urlpatterns = [
    # path('snippets/', snippet_list),
    # path('snippets/<int:pk>/', snippet_detail),

    # Class-based-view 를 사용하는 경우, as_view()함수를 호출
    path('snippets/', apis.SnippetListCreateAPIView.as_view()),
]
