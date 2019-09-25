from django import forms
from .models import Article
# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=10, 
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class':'my-title',
#                 'placeholder':'Enter the title',
#             }
#         )
#     )
#     ## models와의 차이점 textfield가 없는대신 사용.
#     content = forms.CharField(
#         widget=forms.Textarea(
#             attrs={
#                 'class':'my-content',
#                 'placeholder':'Enter the content',
#                 'row': 5,
#                 'cols':40,
#             }
#         ),
#         label='내용'
#     ) 

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='제목',
        max_length=10,
        widget=forms.TextInput(
            attrs={
                'class':'my-title',
                'palceholder':'endter the title'
            }
        )
    )
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class':'my-content',
                'placeholder':'Enter the content',
                'row': 5,
                'cols':40,
            }
        ),
        label='내용'
    ) 
    class Meta:
        model = Article
        # fields = ('title','content',...이어서)
        fields = '__all__'
        # exclude = ('title')# title만 제외 할때 

class CommentForm(forms.Form):
    content = forms.CharField(
        max_length=140,
        label='댓글',
        widget=forms.TextInput(
             attrs={
                'class':'my-title',
                'palceholder':'endter the title'
            }
        )
    )
    created_at = forms.DateTimeField()
    updated_at = forms.DateTimeField()
    # class Meta:

        

        
