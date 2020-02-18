from rest_framework import serializers

from .models import Snippets


# Post
#  List         PostSerializer
#  Retrieve     PostDetailSerializer
#  Update       PostUpdateSerializer
#  Create       PostCreateSerializer
class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = (
            'pk',
            'author',
            'title',
            'code',
            'linenos',
            'language',
            'style',
            'created',
        )


class SnippetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = (
            'title',
            'code',
            'linenos',
            'language',
            'style',
            'created',
        )

    def to_representation(self, instance):
        return SnippetSerializer(instance).data
