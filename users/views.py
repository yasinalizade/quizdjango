from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpRequest
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import CreationForm
from .models import User

EMOJI_CHOICE = (
    "img/emoji/haloween.svg",
    "img/emoji/santa.svg",
    "img/emoji/bronzemedal.svg",
    "img/emoji/silvermedal.svg",
    "img/emoji/goldmedal.svg",
)


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("quiz:index")
    template_name = "users/signup.html"


@login_required
def index(request: HttpRequest) -> HttpResponse:
    users = User.objects.all().order_by("-scores")
    context = {
        "users": users,
    }
    return render(request, "users/index.html", context)


@login_required
def profile(request: HttpRequest) -> HttpResponse:
    return render(request, "users/profile.html")


@login_required
def buy(
    request: HttpRequest, price: int, color=None, emoji_id=None
) -> HttpResponse:
    user = User.objects.get(id=request.user.id)
    try:
        user.scores -= price
        if emoji_id is None:
            user.color = color
        if color is None:
            user.emoji = EMOJI_CHOICE[emoji_id]
        user.save()
    except Exception:
        return render(request, "users/failed.html")
    return redirect("/auth/profile/")
