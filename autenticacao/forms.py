from django import forms
from allauth.account.forms import SignupForm
from django.forms.widgets import DateInput

class CustomSignup(SignupForm):
    first_name = forms.CharField(max_length=30, required=True, label="Primeiro Nome")
    last_name = forms.CharField(max_length=30, required=True, label="Sobrenome")
    data_nascimento = forms.DateField(
        required=True, 
        label="Data de Nascimento", 
        widget=DateInput(attrs={'type': 'date'})
    )
    numero_telefone = forms.CharField(required=True, label="Número de Telefone")

    def save(self, request):
        user = super(CustomSignup, self).save(request)

        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.data_nascimento = self.cleaned_data['data_nascimento']
        user.numero_telefone = self.cleaned_data['numero_telefone']

        user.save()
        return user