from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import snippet_list, snippet_detail

from .apis import api_view, mixins, generics, viewsets

app_name = 'snippets'

router = DefaultRouter()
router.register(r'snippets', viewsets.SnippetViewSet)

urlpatterns_api_view = [
    # path('snippets/', snippet_list),
    # path('snippets/<int:pk>/', snippet_detail),

    # Class-based-view 를 사용하는 경우, as_view()함수를 호출
    # path('snippets/', api_view.SnippetListCreateAPIView.as_view()),
    # path('snippets/<int:pk>/', api_view.SnippetRetrieveUpdateDestroyAPIView.as_view()),
    path('snippets/', generics.SnippetListCreateAPIView.as_view()),
    path('snippets/<int:pk>/', generics.SnippetRetrieveUpdateDestroyAPIView.as_view()),
]

urlpatterns_viewset = [
    path('snippets/', viewsets.SnippetViewSet.as_view({
        'get': 'list',
        'create': 'create',
    })),
    path('snippets/<int:pk>/', viewsets.SnippetViewSet.as_view({
        'get': 'retrieve',
        'patch': 'partial_update',
        'delete': 'destroy',
    })),
]

urlpatterns = [
    path('api-view/', include(urlpatterns_api_view)),
    path('viewset/', include(urlpatterns_viewset)),
    path('router/', include(router.urls)),
]
