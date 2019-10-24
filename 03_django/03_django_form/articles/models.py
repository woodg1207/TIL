from django.db import models
from django.urls import reverse
from django.conf import settings
# Create your models here.
class Hashtag(models.Model):
    ## article model 보다 상위에 존재해야 한다.
    content = models.TextField(unique=True)

    def __str__(self):
        return self.content


class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #1:N(user:article)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
        )
    #N:M
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name='like_articles', 
        blank=True
        )
    # blank=True : 빈 값도 허용을 시켜줌. 
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    
    
    class Meta:
        ordering = ('-pk',)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("articles:detail", kwargs={"article_pk": self.pk})

class Comment(models.Model):
    #1:N article:comment
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-pk', )

    def __str__(self):
        return self.content 