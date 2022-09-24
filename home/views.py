from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = 'notes/list'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'
    

class HomeView(TemplateView):
    template_name ='home/welcome.html'
    today = datetime.today()
    extra_context = {'today':today}


class AuthorizedView(LoginRequiredMixin, TemplateView):
    template_name = 'home/authorized.html'
    login_url='home/login.html'


