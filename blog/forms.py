from django import forms

from .models import Comment, Post


class CommentForm(forms.ModelForm):

        class Meta:
            model = Comment
            fields = ('email', 'body',)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'title','category',]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['body'].label = "Text"
        self.fields['title'].label = "Title"
        self.fields['category'].label = "Category"
        self.fields['category'].widget.attrs.update({'class': 'select'})
        # self.fields['body'].widget.attrs.update({'class': 'comment'})
        # self.fields['title'].widget.attrs.update({'class': 'comment'})
        self.fields['category'].empty_label = "Select Category"
