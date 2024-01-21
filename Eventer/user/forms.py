from django import forms
from . models import Users

class userForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['first_name','username','last_name','email','phone','password']