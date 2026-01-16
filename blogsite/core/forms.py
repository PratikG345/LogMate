from django import forms
from .models import Log

class Form(forms.ModelForm):
    class Meta:
        model = Log
        fields = "__all__"
