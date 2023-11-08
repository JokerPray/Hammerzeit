from django.contrib.auth.decorators import login_required
from django.shortcuts import render



# Create your views here.

def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123']
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


@login_required
def profile_view(request):
    return render(request, 'main/profile.html')



