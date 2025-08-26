from django.db import models
from django.utils.translation import gettext_lazy as _


class EdificioStatus(models.TextChoices):
    ACTIVE = "active", _("Activo")
    INACTIVE = "inactive", _("Baja")
    UNDER_CONSTRUCTION = "under_construction", _("En construcción")


class Edificio(models.Model):
    code = models.CharField(
        _("Código"),
        max_length=10,
        unique=True,
        help_text=_("Código corto único, p. ej. ARE, VDP."),
    )
    name = models.CharField(
        _("Nombre"),
        max_length=120,
        help_text=_("Nombre descriptivo del edificio."),
    )
    address = models.CharField(
        _("Dirección"),
        max_length=200,
        blank=True,
        help_text=_("Dirección completa."),
    )
    status = models.CharField(
        _("Estado"),
        max_length=20,
        choices=EdificioStatus.choices,
        default=EdificioStatus.ACTIVE,
    )
    created_at = models.DateTimeField(_("Creado"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Actualizado"), auto_now=True)

    class Meta:
        ordering = ["code"]
        verbose_name = _("Edificio")
        verbose_name_plural = _("Edificios")

    def __str__(self):
        return f"{self.code} — {self.name}"

    def save(self, *args, **kwargs):
        if self.code:
            self.code = self.code.strip().upper()
        super().save(*args, **kwargs)


class Sectores(models.Model):
    edificio = models.ForeignKey(
        "data_admin.Edificio",
        verbose_name=_("Edificio"),
        on_delete=models.PROTECT,
        related_name="sectores",
    )
    nombre = models.CharField(_("Sector"), max_length=100)
    descripcion = models.TextField(_("Descripción"), blank=True)

    class Meta:
        ordering = ["nombre"]
        verbose_name = _("Sector")
        verbose_name_plural = _("Sectores")

    def __str__(self):
        return self.nombre
