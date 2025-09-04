from typing import Any

from django import forms

from .models import Edificio


class EdificioForm(forms.ModelForm):
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)

    class Meta:
        model = Edificio
        fields = ["code", "name", "address", "status"]
        widgets = {
            "code": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Código único"}
            ),
            "name": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre del edificio"}
            ),
            "address": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Dirección completa"}
            ),
            "status": forms.Select(attrs={"class": "form-control"}),
        }
        help_texts = {
            "code": "Código corto único, p. ej. ARE, VDP.",
            "name": "Nombre descriptivo del edificio.",
            "address": "Dirección completa.",
        }
