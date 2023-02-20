from django.contrib import admin
from django.contrib.admin import ModelAdmin

from store.models import Book


# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(ModelAdmin):
    pass
