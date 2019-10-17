from django.urls import path
from . import views

app_name = 'article'
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('detail/<int:pk>/delete/', views.delete, name='delete'),
    path('detail/<int:pk>/update/', views.update, name='update'),
    path('detail/<int:article_pk>/comment/', views.comment_create, name='comment_create'),
    path('detail/<int:article_pk>/comment/<int:comment_pk>', 
    views.comment_delete, name='comment_delete'),
    
    
]