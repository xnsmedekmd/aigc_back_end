from django.db import models
import pinyin

class Content(models.Model):
    """内容基类模型"""
    CONTENT_TYPE_CHOICES = [
        ('poetry', '古诗'),
        ('prose', '古文'),
    ]
    
    title = models.CharField(max_length=100, verbose_name="标题")
    author = models.CharField(max_length=50, verbose_name="作者")
    dynasty = models.CharField(max_length=50, verbose_name="朝代")
    content = models.TextField(verbose_name="内容")
    translation = models.TextField(verbose_name="翻译")
    type = models.CharField(max_length=10, choices=CONTENT_TYPE_CHOICES, verbose_name="内容类型")
    cover_image = models.CharField(max_length=255, verbose_name="封面图片路径")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    
    class Meta:
        abstract = True
    
    def get_video_url(self):
        """获取视频URL，使用诗词首字拼音命名"""
        if not self.title:
            return ""
        
        # 获取标题首字的拼音
        first_char = self.title[0]
        first_char_pinyin = pinyin.get(first_char, format="strip", delimiter="")
        
        # 构建视频URL
        type_folder = 'poetry' if self.type == 'poetry' else 'prose'
        return f"/classical_literature/static/videos/{type_folder}/{first_char_pinyin}.mp4"
        
class Poetry(Content):
    """古诗模型"""
    video_url = models.CharField(max_length=255, verbose_name="视频URL")
    
    def __str__(self):
        return f"{self.title} - {self.author}"
    
    def save(self, *args, **kwargs):
        # 在保存前自动生成视频URL
        if not self.video_url:
            self.video_url = self.get_video_url()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "古诗"
        verbose_name_plural = "古诗"

class Prose(Content):
    """古文模型"""
    video_url = models.CharField(max_length=255, verbose_name="视频URL")
    annotation = models.JSONField(default=list, blank=True, verbose_name="注释")
    appreciation = models.TextField(blank=True, verbose_name="赏析")
    
    def __str__(self):
        return f"{self.title} - {self.author}"
    
    def save(self, *args, **kwargs):
        # 在保存前自动生成视频URL
        if not self.video_url:
            self.video_url = self.get_video_url()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "古文"
        verbose_name_plural = "古文"
