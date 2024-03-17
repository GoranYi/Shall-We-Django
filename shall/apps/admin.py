from django.contrib import admin
from .models import Wiki

# class WikiAdmin(admin.ModelAdmin):
#     search_fields = ['title']

admin.site.register(Wiki)
