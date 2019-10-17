from django.shortcuts import render, redirect
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {'articles':articles,}
    return render(request, 'articles/index.html', context)

def create(request):

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            # title = request.POST.get('title') 
            # content = request.POST.get('content')
            # article = Article(title=title, content=content)
            # article.save()
            article = form.save()
            # return redirect('article:index')
            return redirect(article)
    else:
        form = ArticleForm()
    context = {'form':form}
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comments = article.comment_set.all()
    context = {'article':article, 'comments':comments,}
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('article:index')

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()    
        return redirect('article:detail', article.pk)
    else:
        context = {'article':article}
        return render(request,'articles/update.html', context)

def comment_create(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method=='POST':
        content = request.POST.get('comment')
        comment = Comment(article=article, content=content)
        comment.save()
        return redirect(article) ##
    else:
        return redirect(article) ##수정

def comment_delete(request, article_pk, comment_pk):
    if request.method == 'POST':
        comment = Comment.objects.get(pk=comment_pk)
        comment.delete()
    return redirect('article:detail', article_pk)


