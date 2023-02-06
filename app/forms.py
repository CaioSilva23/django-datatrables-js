from django import forms
from .models import Pessoa

class FormPessoa(forms.ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

        # widgets = {
        #     'data_nascimento': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        # }