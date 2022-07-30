from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number', 'date', 'time')
    search_fields = ('email', 'phone_number')
    date_hierarchy = 'date'