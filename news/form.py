from django import forms
from news.models import Comment_news


class Comment_news_Form(forms.ModelForm):
    class Meta:
        model = Comment_news
        fields = ('name', 'email', 'comment')
