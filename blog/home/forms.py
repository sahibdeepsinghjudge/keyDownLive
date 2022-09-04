from django import forms
from .models import *
from ckeditor.fields import RichTextField

class blogForm(forms.ModelForm):
    blog_content = RichTextField()
    class Meta:
        model  = blog
        fields = ('blog_content',)