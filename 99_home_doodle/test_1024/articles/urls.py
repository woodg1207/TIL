from django.urls import path, include
from . import views
app_name='articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:article_pk>/detail/', views.detail, name='detail'),
    path('<int:article_pk>/delete/', views.delete, name='delete'),
    path('<int:article_pk>/update/', views.update, name='update'),
    path('<int:article_pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:article_pk>/delete/<int:comment_pk>', views.comment_delete, name='comment_delete'),
]