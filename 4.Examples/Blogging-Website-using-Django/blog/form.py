#This file is only required while using external form rather than default django and add some style:
#In such case we have to make some changes to view and class mb-3 tag from bootstrap
from django import forms
from .models import Post,Comment
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','topic','author','header_image')
        Widgets = {

            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),

        }
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }