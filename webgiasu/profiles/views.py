import django
from django.contrib.auth import forms, tokens
from django.forms import fields, widgets
from django.http import request
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView, LogoutView  
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.shortcuts import redirect
from django.urls import reverse
from django import forms
from captcha.fields import ReCaptchaField
from django.views.generic.edit import UpdateView
from profiles.form import RegisterForm, LoginForm
from profiles.form import ProfileEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.conf import settings
import pprint

User = get_user_model()

class SiteLoginView(LoginView):
    template_name = 'login.html'
    form_class = LoginForm
    

class SiteRegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm

    def form_valid(self, form):
        data = form.cleaned_data
        print(data['username'],data['password1'],data['email'])
        print(len(data['username']),len(data['password1']),len(data['email']))
        new_user = User.objects.create_user(username = data['username'], password = data['password1'], email = data['email'], is_verified=False)
        try:
            token = account_activation_token.make_token(new_user)
            new_user.token = token
            new_user.save()
            link = f'{settings.MY_DOMAIN}/verify/{token}'
            send_mail('TMVIETNGA confirm email:',
                    ' Hi, you have ergistered with tmvietnga.com by this email.\n to confirm, click following link:\n '+ link,
                    'anewday19991@gmail.com',
                    [data['email']],
                    fail_silently=False,
                )
        except Exception as e:
            print(e)
        url = f"{reverse('register_ok')}?username={new_user.username}&email={new_user.email}"
        return redirect(url)

def verify(request, token):
    try:
        user = User.objects.all().filter(token=token)
        if user:
            if user.first().is_verified:
                return render(request, 'success_verify.html', {'msg' : 'Already confirmed.'})
            user.update(is_verified = True)
        else:
            return render(request, 'success_verify.html', {'msg' : 'Not exist.'})
        return render(request, 'success_verify.html', {'msg' : 'Successfully.'})
    except Exception as e:
        print(e)
        return render(request, 'success_verify.html', {'msg' : str(e)})

class SiteRegisterOk(TemplateView):
    template_name = 'register_ok.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.GET.get('username')
        return context

'''class EditProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profiles.html'''

class SiteLogoutView(LogoutView):
    template_name = 'home.html'

@login_required
def ProfileEditView(request):
    if request.method == 'POST':
        p_form  = ProfileEditForm(request.POST, request.FILES, instance=request.user)
        '''print("++++++")
        print(request.POST)
        print(request.FILES)'''
        
        if p_form.is_valid():
            old_avatar = User.objects.filter(username=request.user.username).first().avatar
            if request.FILES != {} and 'default95486216548123654894126.png' not in old_avatar.url:
                print("XOA")
                old_avatar.storage.delete(old_avatar.name)
            p_form.save()
            messages.success(request, f'Đã lưu ✓')
            return redirect('profile')
    else:
        p_form  = ProfileEditForm(instance=request.user)

    context = {
        'p_form' : p_form,
        'nav' : 'profile',
    }
    return render(request, 'profiles.html', context)