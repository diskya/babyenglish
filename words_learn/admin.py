from django.contrib import admin
from .models import Word, Library



class WordAdmin(admin.ModelAdmin):
    list_per_page = 50
    list_display = ['text', 'translate', 'id', 'add_date']
    # fields=['text', 'proficiency', 'idle_time']
    readonly_fields = ("add_date","id")

admin.site.register(Word, WordAdmin)
admin.site.register(Library)
