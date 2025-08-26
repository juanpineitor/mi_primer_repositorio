from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.cache import never_cache

# Create your views here.


@login_required
@never_cache
def home(request):
    return render(request, "core/home.html")
