"""webgiasu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.db import router
from django.urls import path, include
from django.views.generic import TemplateView

from django.conf import Settings, settings
from django.conf.urls.static import static

from basic_stt import views as views_basic
from profiles import views as profiles_views

from tutor import views as views_tutor
from market import views as views_market
from employee import views as views_employee
from homework import views as views_homework

from django.contrib.auth import views as auth_views
from rest_framework import routers
from myapi.views import marketpostViewSet

from django.conf.urls import url
from vote.views import VoteListView

urlpatterns = [

    path('adminthanhthiencontrol/', admin.site.urls),
    path('', views_basic.home_view, name='home'),
    #path('', include('market.urls')),
    path('about/', views_basic.about, name='about'),
   
    #path('accounts/', include('django.contrib.auth.urls')),
    path('login/', profiles_views.SiteLoginView.as_view(extra_context={'nav': 'login'}), name='login'),
    path('register/', profiles_views.SiteRegisterView.as_view(extra_context={'nav': 'register'}), name='register'),
    path('register/ok/', profiles_views.SiteRegisterOk.as_view(), name='register_ok'),
    path('verify/<str:token>', profiles_views.verify, name='verify'),

    path('profile/', profiles_views.ProfileEditView, name='profile'),
    path('logoutok/', profiles_views.SiteLogoutView.as_view(), name='logout_ok'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    #tutor
    path('findtutor/', views_tutor.FindTutor, name='findtutor'),
    path('findtutor_mypost/', views_tutor.FindTutorMypost, name='findtutor_mypost'),
    #market
    path('market/', views_market.Market, name='market'),
    path('market_mypost/', views_market.MarketMypost, name='market_mypost'),
    #employee
    path('employee/', views_employee.Employee, name='employee'),
    path('employee_mypost/', views_employee.EmployeeMypost, name='employee_mypost'),
    #homework
    path('homework/', views_homework.Homework, name='homework'),
    path('homework_mypost/', views_homework.HomeworkMypost, name='homework_mypost'),


    #tutor
    path('showinfo/', views_tutor.get_user_info, name='showinfo'),
    path('getcontact/', views_tutor.get_post_contact, name='getcontact'),
    path('getpostpost/', views_tutor.get_post_post, name='getpostpost'),
    path('reportpost/', views_tutor.report_post, name='reportpost'),
    #path('getpage/', views_tutor.get_page, name='getpage'),
    path('deletepost/', views_tutor.delete_post, name='deletepost'),
    path('editpost/', views_tutor.edit_post, name='editpost'),
    path('notice/', views_tutor.notice, name='notice'),
    #market
    path('market_showinfo/', views_market.get_user_info, name='market_showinfo'),
    path('market_getcontact/', views_market.get_post_contact, name='market_getcontact'),
    path('market_getpostpost/', views_market.get_post_post, name='market_getpostpost'),
    path('market_reportpost/', views_market.report_post, name='market_reportpost'),
    #path('getpage/', views_tutor.get_page, name='getpage'),
    path('market_deletepost/', views_market.delete_post, name='market_deletepost'),
    path('market_editpost/', views_market.edit_post, name='market_editpost'),
    path('market_notice/', views_market.notice, name='market_notice'),
    #employee
    path('employee_showinfo/', views_employee.get_user_info, name='employee_showinfo'),
    path('employee_getcontact/', views_employee.get_post_contact, name='employee_getcontact'),
    path('employee_getpostpost/', views_employee.get_post_post, name='employee_getpostpost'),
    path('employee_reportpost/', views_employee.report_post, name='employee_reportpost'),
    #path('getpage/', views_tutor.get_page, name='getpage'),
    path('employee_deletepost/', views_employee.delete_post, name='employee_deletepost'),
    path('employee_editpost/', views_employee.edit_post, name='employee_editpost'),
    path('employee_notice/', views_employee.notice, name='employee_notice'),
    #homework
    path('homework_showinfo/', views_homework.get_user_info, name='homework_showinfo'),
    path('homework_getcontact/', views_homework.get_post_contact, name='homework_getcontact'),
    path('homework_getpostpost/', views_homework.get_post_post, name='homework_getpostpost'),
    path('homework_reportpost/', views_homework.report_post, name='homework_reportpost'),
    #path('getpage/', views_tutor.get_page, name='getpage'),
    path('homework_deletepost/', views_homework.delete_post, name='homework_deletepost'),
    path('homework_editpost/', views_homework.edit_post, name='homework_editpost'),
    path('homework_notice/', views_homework.notice, name='homework_notice'),

    #For web subject
    #API
    path('api-auth/', include('rest_framework.urls'))

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
