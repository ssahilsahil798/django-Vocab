from django.contrib import admin

# Register your models here.

from cardapp.models import CardCategory, Word

admin.site.register(CardCategory)
admin.site.register(Word)
