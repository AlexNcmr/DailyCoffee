from django import forms

class UserForm(forms.Form):
    kindle_email = forms.EmailField(label='Kindle Email', max_length=100)
    user_email = forms.EmailField(label='Personal Email', max_length=100)
    data_source = forms.CharField(label='Enter HN for HackerNews or your favorite subreddit by (/r/SUBREDDITNAME)', max_length=100)
    
