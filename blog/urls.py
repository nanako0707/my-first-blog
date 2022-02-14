from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    # post_list という名前のビューをルートURL に割り当てる
    # このURLパターンは空の文字列に一致する=Django はビューを見つける時、URLのパス（path）の前にくっつくドメイン名を無視する
    # http://127.0.0.1:8000/ というアドレスにアクセスしてきたら、views.post_list が正しい行き先だということをDjango に伝える
    # name='post_list' は、ビューを識別するために使われるURL の名前
    path('', views.post_list, name='post_list'),
    # post_detail という名前のビューを'post/<int:pk>/' に割り当てる
    # (例)http://127.0.0.1:8000/post/5 というアドレスにアクセスしてきたら、views.post_detail が正しい行き先だということをDjango に伝える
    # name='post_list' は、ビューを識別するために使われるURL の名前
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit')
]