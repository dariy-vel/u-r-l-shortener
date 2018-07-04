from django import forms
from .models import LongToShort


class AddLongURLForm(forms.ModelForm):
    class Meta:
        model = LongToShort
        fields = ['long_url', 'name']