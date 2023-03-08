from django.shortcuts import render
from allauth.account.views import PasswordChangeView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy


class CustomChangePassword(PasswordChangeView, SuccessMessageMixin):
    success_message = 'your password account changed successfully'
    success_url = reverse_lazy('book_list')


class CustomResetPassword(PasswordResetView, SuccessMessageMixin):
    success_message = 'your password account is reset'
    success_url = reverse_lazy('account_login')

