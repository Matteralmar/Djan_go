from django.forms import ModelForm, TextInput

from .models import Post, Subscriber, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'content']
        widgets = {
            "title": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Name of post",
            }),
            "description": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Description",
            }),
            "content": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Content",
            }),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            "comment": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your comment",
            }),
        }


class SubscriberForm(ModelForm):
    # author_id = forms.ModelChoiceField(
    # queryset=Author.objects.all().order_by('name'),
    # empty_label='Pick an author',
    # widget=forms.Select(attrs={
    #           "class": "form-control"
    #       })
    #   )

    class Meta:
        model = Subscriber
        fields = ["email_to", "author_id"]
        widgets = {
            "email_to": TextInput(attrs={
                "class": "form-control",
                "placeholder": "Email",
            }),
            "author_id": TextInput(attrs={
                "class": "form-control",
                "placeholder": "User name",
            }),
        }
