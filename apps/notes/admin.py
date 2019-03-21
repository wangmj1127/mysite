from django.contrib import admin
from apps.notes.models import Note,NoteComment,WishList
# Register your models here.

admin.site.register(Note)
admin.site.register(NoteComment)
admin.site.register(WishList)
