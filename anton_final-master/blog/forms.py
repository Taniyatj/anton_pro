from django import forms
from .models import Post




class PostForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))
    class Meta:
        model = Post
        fields = ('title', 'text','category','image')
        
      
     

    



 



