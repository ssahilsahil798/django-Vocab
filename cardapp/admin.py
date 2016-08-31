from django.contrib import admin

# Register your models here.

from cardapp.models import CardCategory, Word, LearntWords

admin.site.register(CardCategory)
admin.site.register(Word)
admin.site.register(LearntWords)
