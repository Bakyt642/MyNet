from django import forms
from django.contrib.auth.models import User
from django.db.models import ImageField
from django.forms import ModelForm

from .models import Profile
from django.forms.widgets import ClearableFileInput

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

# class MyClearableFileInput(ClearableFileInput):
#     initial_text = 'w'
#     input_text = 'w'
#     clear_checkbox_label = 'w'
#
# class EditProfileForm(ModelForm):
#     image = ImageField(label='Select Profile Image',required = False, widget=MyClearableFileInput)



class ProfileEditForm(forms.ModelForm):



    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args,**kwargs)
        self.fields['photo'].label ="Avatar"
        self.fields['photo'].widget.attrs.update({'class': 'form-control-2'})
        # self.fields['photo'].widget.clear_checkbox_label({'class': 'form-control-2'})
        self.fields['photo'].widget.clear_checkbox_label = ""
        self.fields['photo'].widget.initial_text = ""
        self.fields['photo'].widget.input_text = ""



    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')

