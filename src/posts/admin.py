from django.contrib import admin
from posts.models import BookPost

class BookPostAdmin(admin.ModelAdmin):
    list_display = ("title", "book_author", "published", "created_on", "last_updated", "score")
    list_editable = ("published",)

admin.site.register(BookPost, BookPostAdmin)
