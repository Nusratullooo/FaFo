from django.urls import path
from news import views

urlpatterns = [
    path('news/', views.news, name='news'),
    path('news_detail/<int:id>', views.news_detail, name='news_detail'),
    path('comment_news/<int:id>', views.comment_news, name='comment_news')
]
