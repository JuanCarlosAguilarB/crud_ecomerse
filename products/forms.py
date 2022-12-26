from django import forms
from .models import Fruits


class FruitsForm(forms.ModelForm):
    """ Forumolario para realizar crud del modelo fruits"""
    class Meta:
        model = Fruits

        # los campos que se van a usar del modelo
        fields = "__all__"
