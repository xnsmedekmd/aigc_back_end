from rest_framework import serializers
from .models import Poetry, Prose

class PoetrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Poetry
        fields = ['id', 'title', 'author', 'dynasty', 'content', 'translation', 'video_url', 'cover_image']

class ProseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prose
        fields = ['id', 'title', 'author', 'dynasty', 'content', 'translation', 'annotation', 'appreciation', 'video_url', 'cover_image']

class ContentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poetry  # 使用Poetry作为基础模型
        fields = ['id', 'title', 'author', 'dynasty', 'cover_image'] 