from django.contrib import admin
from models import Snippet

class SnippetAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

admin.site.register(Snippet, SnippetAdmin)
