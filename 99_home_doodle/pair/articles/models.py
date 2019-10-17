from django.db import models
from django.urls import reverse
# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        ordering = ['-pk',]
    #     verbose_name = _("")
    #     verbose_name_plural = _("s")

    # def __str__(self):
    #     return self.name

    def get_absolute_url(self):
        return reverse("article:detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-pk',]

    #     verbose_name = ("Comment")
    #     verbose_name_plural = ("Comments")

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("Comment_detail", kwargs={"pk": self.pk})
