from captcha.fields import CaptchaField
from django import forms
from tagging_autocomplete.widgets import TagAutocomplete
from .models import Comment, Post


class CommentForm(forms.ModelForm):
        captcha = CaptchaField()
        class Meta:
            model = Comment
            fields = ('email', 'body',)

class PostForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = ['body', 'title','category','tags']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = "Text"
        self.fields['title'].label = "Title"
        self.fields['tags'].label = "Tags"
        self.fields['category'].label = "Category"
        self.fields['category'].widget.attrs.update({'class': 'select'})
        # self.fields['body'].widget.attrs.update({'class': 'comment'})
        # self.fields['title'].widget.attrs.update({'class': 'comment'})
        self.fields['category'].empty_label = "Select Category"

class SearchForm(forms.Form):
        query = forms.CharField()