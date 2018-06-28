from django.contrib import admin
from .models import Doctor

class AdminDoctor(admin.ModelAdmin):
    list_display = ['nombre', 'rut', 'fecha_nacimiento', 'fecha_ingreso_clinica']

    class Meta:
        model = Doctor


# Register your models here.

admin.site.register(Doctor, AdminDoctor)
