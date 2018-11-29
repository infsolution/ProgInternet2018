from django.forms import ModelForm
from blog.models import Post
from django import forms 

class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'text']

		widgets ={
		'title':forms.TextInput(attrs={'class':'form-control, maxlength:100'}),
		'text':forms.Textarea(attrs={'class':'form-control, maxlength:255'}),
		}