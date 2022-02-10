from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # request: インターネットを介してユーザから受け取った全ての情報が詰まったもの
    # {}: {} の中に指定した情報を、テンプレートが表示してくれる。 {} の中に引数を記述する場合、名前と値をセットにする
    return render(request, 'blog/post_list.html', {'posts': posts})