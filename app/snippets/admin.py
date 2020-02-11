from django.contrib import admin
from .models import Snippets


@admin.register(Snippets)
class SnippetAdmin(admin.ModelAdmin):
    pass
