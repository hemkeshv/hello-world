from django import forms

class UserForm(forms.Form):
    first_name= forms.CharField(max_length=100)
    last_name= forms.CharField(max_length=100)
    team_name = forms.CharField(max_length=100)