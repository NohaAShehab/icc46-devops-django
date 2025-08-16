from django.shortcuts import render
from django.http import HttpResponse

from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm


from django.views.generic import CreateView

from accounts.forms import RegisterForm

# Create your views here.


def profile(request):
    return HttpResponse('profile')


class CreateAccountView(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

