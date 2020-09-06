from django.shortcuts import render
from .models import ArticlePost
# Create your views here.
from django.http import HttpResponse
import markdown

def article_list(request):
    articles = ArticlePost.objects.all()
    context = {'articles': articles }
    return render(request, 'article/list.html', context)

def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)

    article.body = markdown.markdown(article.body,
            extensions=[
                'markdown.extensions.extra',
                'markdown.extensions.codehilite',
                ])

    context = {'article':article}
    return render(request, 'article/detail.html', context)
def article_create(request):
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_vaild():
            new_article = article_post_form.save(commit=False)
            new_article.author = User.objects.get(id=1)
            new_article.save()
            return redirect("article:article_list")
        else:
            return HTTPresponse("表单内有误，请重新填写。")
    else:
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form}
        return render(request,'article/create.html', context)
