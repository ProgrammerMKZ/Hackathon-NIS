from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email")
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)

        if commit==True:
            user.save()
        return user