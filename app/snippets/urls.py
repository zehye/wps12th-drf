from django.urls import path
from .views import snippet_list

app_name = 'snippets'
urlpatterns = [
    path('snippets/', snippet_list),
]