from django.urls import path
from core.login.views import LoginFormView, LogoutView, LogoutRedirectView, LoginFormView2

urlpatterns = [
    path('', LoginFormView2.as_view(), name='login'),
    path('2', LoginFormView.as_view(), name='login2'),
    #path('logout/', LogoutView.as_view(), name='logout'),
    path('logout/', LogoutRedirectView.as_view(), name='logout'),
]