from django import forms
from django.forms import ModelForm

from app.models import Post


class Registration(forms.Form):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    contact_ph = forms.CharField(max_length=15)
    pswd = forms.CharField(max_length=30)
    conf_pswd = forms.CharField(max_length=30)
    place = forms.CharField(max_length=30)



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('Title','Description','title_tag','author','category',)

        widgets = {
            'Title': forms.TextInput(attrs={'class': 'form-control'}),
            'Description': forms.Textarea(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value': '','id':'elder','type':'hidden'}),
            'category': forms.TextInput(attrs={'class': 'form-control'}),



        }