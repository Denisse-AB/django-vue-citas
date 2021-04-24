from .models import Post
from rest_framework import serializers

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['email', 'name', 'tel', 'date', 'time']
