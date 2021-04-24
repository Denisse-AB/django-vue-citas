from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'tel', 'date', 'time')
    search_fields = ['tel']
    date_hierarchy = 'date'

