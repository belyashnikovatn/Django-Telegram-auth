from django.shortcuts import render

from DTAproject.settings import BOT_NAME


def index(request):

    context = {
        'data': 'users',
        'BOT_NAME': BOT_NAME
    }

    return render(request, 'index.html', context)
