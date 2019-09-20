from django.urls import reverse
from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        

    def get_absolute_url(self):
        # return reverse('articles:detail', args=[self.pk]) 같은 것,,, reverse는 문자열로 나온다. 
        return reverse('articles:detail', kwargs={'article_pk':self.pk}) #views.py에 있는 함수의 pk를 키값으로
        #주의사항
        #reverse 함수에 args랑 kwargs를 동시에 인자로 보낼 수 없다. 
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE) 
    # n:m 관계에선 related_name='comments'을 사용 1:n에선 사용을 권장하지 않음'article_id'를 그대로 사용
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-pk']

    def __str__(self):
        return f'<Article({self.article_id}): Coment({self.pk})-{self.content}>'



