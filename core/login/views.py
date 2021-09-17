from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
import config.settings as setting
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.generic import FormView, RedirectView
from core.login.forms import FormLogin


#class Login(FormView):
#    template_name = 'login.html'
#    form_class = FormLogin
#    success_url = reverse_lazy('contact_list')
#
#    @method_decorator(csrf_protect)
#    @method_decorator(never_cache)
#    def dispatch(self, request, *args, **kwargs):
#        if request.user.is_authenticated:
#            return HttpResponseRedirect(self.get_success_url())
#        else:
#            return super(Login, self).dispatch(request, *args, **kwargs)
#
#    def form_valid(self, form):
#        login(self.request, form.get_user())
#        return super(Login, self).form_valid(form)
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['tittle'] = 'Iniciar sesión'
#        return context


class LoginFormView2(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(setting.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tittle'] = 'Iniciar sesión'
        return context

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url = reverse_lazy(setting.LOGIN_REDIRECT_URL)

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar sesión'
        return context


class LogoutRedirectView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)