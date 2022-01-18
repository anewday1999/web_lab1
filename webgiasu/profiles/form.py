from django.contrib.auth import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
from captcha.fields import ReCaptchaField
from django.db.models import fields
from django.forms.fields import CharField
from django.utils.translation import gettext, gettext_lazy as _
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
from django.contrib.auth.forms import (
    AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm,
)
from django.contrib.auth import (
    authenticate, get_user_model, password_validation,
)

User = get_user_model()

class LoginForm(AuthenticationForm):
    captcha = ReCaptchaField()
    username = UsernameField(label=_("Login"),widget=forms.TextInput(attrs={'autofocus': True, 'class':'d-flex border rounded', 'style':'background-color:#FFFFFF;'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'class':'d-flex border rounded', 'style':'background-color:#FFFFFF;'}),
    )
    error_messages = {
        'invalid_login': _(
            "Thông tin đăng nhập không đúng."
        ),
        'inactive': _("Tài khoản chưa kích hoạt."),
    }

class RegisterForm(UserCreationForm):
    error_messages = {
        'password_mismatch': mark_safe(_(
            '<small style="color:#e60000"> Password not match.</small>'
        )),
        'password_tooshort':mark_safe(_(
            '<small style="color:#e60000">Minimum is 8 characters.</small>'
        )),
    }
    #email = forms.EmailField()
    email = forms.EmailField(required=True,
            widget=forms.EmailInput(attrs={'required': True, 'class':'col-4 d-flex border rounded', 'style':'background-color:#FFFFFF;'}),
            )
    captcha = ReCaptchaField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'captcha')
        field_classes = {'username': UsernameField}
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        if len(password1) < 8:
            raise ValidationError(
                self.error_messages['password_tooshort'],
                code='password_tooshort',
            )
        return password2
class ProfileEditForm(forms.ModelForm):
    avatar = forms.ImageField(label=_('Avatar:'),required=False, error_messages = {'invalid':_("Image files only")}, widget=forms.FileInput)
    class Meta:
        model = User
        fields = ('full_name', 'address', 'school', 'specialize', 'yearofschool', 'sexs', 'years_of_birth', 'more', 'avatar')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'full_name' in self.fields:
            self.fields['full_name'].widget.attrs['class'] = 'col-4 d-flex'
        if 'address' in self.fields:
            self.fields['address'].widget.attrs['class'] = 'col-4 d-flex'
        if 'school' in self.fields:
            self.fields['school'].widget.attrs['class'] = 'col-4 d-flex'
        if 'specialize' in self.fields:
            self.fields['specialize'].widget.attrs['class'] = 'col-4 d-flex'
        if 'yearofschool' in self.fields:
            self.fields['yearofschool'].widget.attrs['class'] = 'col-4 d-flex'
        if 'sexs' in self.fields:
            self.fields['sexs'].widget.attrs['class'] = 'col-4 d-flex'
        if 'years_of_birth' in self.fields:
            self.fields['years_of_birth'].widget.attrs['class'] = 'col-4 d-flex'
        if 'more' in self.fields:
            self.fields['more'].widget.attrs['class'] = 'col-4 d-flex'
            