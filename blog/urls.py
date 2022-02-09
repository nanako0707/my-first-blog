from django.urls import path
from . import views

urlpatterns = [
    # post_list という名前のビューをルートURL に割り当てる
    # このURLパターンは空の文字列に一致する=Django はビューを見つける時、URLのパス（path）の前にくっつくドメイン名を無視する
    # http://127.0.0.1:8000/ というアドレスにアクセスしてきたら、views.post_list が正しい行き先だということをDjango に伝える
    # name='post_list' は、ビューを識別するために使われるURL の名前
    path('', views.post_list, name='post_list'),
]