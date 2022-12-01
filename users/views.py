from django.views.generic import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import CreationForm
from .models import User


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('quiz:index')
    template_name = 'users/signup.html'


def index(request):
    users = User.objects.all()
    context = {
        'users': users,
    }
    return render(request, 'users/index.html', context)
