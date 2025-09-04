from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def index(request: HttpRequest) -> HttpResponse:
    """Vista para mostrar el index de administración de usuarios."""
    usuarios = User.objects.all()
    return render(request, "data_admin/index.html", {"usuarios": usuarios})
