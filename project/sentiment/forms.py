from django import forms
from .models import File


class MyForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ["filename", "file", ]
        labels = {'filename': "File Name", "file": "File", }