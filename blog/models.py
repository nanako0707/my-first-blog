from cgitb import text
from pyexpat import model
from time import time
from turtle import title
from django.conf import settings
from django.db import models
from django.utils import timezone

# models.Model はPost がDjango Model だという意味。Django が、これはデータベースに保存するべきものだと分かるようにしている。
class Post(models.Model):
    # models.ForeignKey 他のモデルへのリンク
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # models.CharField 文字数が制限されたテキストを定義するフィールド
    title = models.CharField(max_length=200)
    # models.TextField 制限なしの長いテキスト用
    text = models.TextField()
    # models.DateTimeField 日付と時間のフィールド
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title