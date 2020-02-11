from rest_framework import serializers
from .models import LANGUAGE_CHOICES, STYLE_CHOICES, Snippets


class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = ['pk', 'title', 'code', 'linenos', 'language', 'style', 'created']
