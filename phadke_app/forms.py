
from django import forms
from phadke_app.models import Posts

class AddPostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = "__all__"  