from django import forms
from .models import Expediente


class ExpedienteForm(forms.ModelForm):
    class Meta:
        model = Expediente
        fields = ["numero_expediente", "anio", "caratula", "Juzgado"]