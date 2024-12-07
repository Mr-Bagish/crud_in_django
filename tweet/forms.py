from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tweet.models import tweet

class TweetForm(forms.ModelForm):
    
    class Meta:
        model = tweet
        fields = ("text","photo")
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your tweet...'}),
            'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class userregister(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
