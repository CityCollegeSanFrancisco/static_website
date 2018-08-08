from django.contrib import admin

# Register your models here.

from .models import Contributor, Editor, Post, Tag

admin.site.register(Contributor)
admin.site.register(Editor)
#admin.site.register(Post)
admin.site.register(Tag)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'updated','display_contributors')
