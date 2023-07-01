from django.contrib import admin

from .models import Note,Grade,Subject,Chapter

# Register your models here.
admin.site.register(Note)
admin.site.register(Grade)
admin.site.register(Subject)
admin.site.register(Chapter)