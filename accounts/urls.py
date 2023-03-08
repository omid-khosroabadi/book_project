from django.urls import path
from . import views


urlpatterns = [
    path('change_password/', views.CustomChangePassword.as_view(), name='account_change_password'),
    path('reset_password/', views.CustomResetPassword.as_view(), name='account_reset_password'),
]


