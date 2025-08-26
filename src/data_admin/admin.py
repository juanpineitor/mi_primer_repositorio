from django.contrib import admin

from .models import Edificio


@admin.register(Edificio)
class EdificioAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "status", "address", "created_at", "updated_at")
    list_display_links = ("code", "name")  # <-- asegura link a edición
    search_fields = ("code", "name", "address")
    list_filter = ("status", "created_at")
    ordering = ("code",)
    readonly_fields = ("created_at", "updated_at")

    fieldsets = (
        ("Identificación", {"fields": ("code", "name", "status")}),
        ("Ubicación", {"fields": ("address",)}),
        (
            "Trazabilidad",
            {"fields": ("created_at", "updated_at"), "classes": ("collapse",)},
        ),
    )
