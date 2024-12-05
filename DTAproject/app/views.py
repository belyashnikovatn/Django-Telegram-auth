from django.shortcuts import get_object_or_404, render

from DTAproject.settings import BOT_NAME
from app.models import User


def index(request):

    context = {
        'BOT_NAME': BOT_NAME,
    }

    return render(request, 'index.html', context)


def user(request, tlg_id):
    user = get_object_or_404(User, tlg_id=tlg_id)

    context = {
        'user': user,
        'tlg': True
    }

    return render(request, 'index.html', context)
