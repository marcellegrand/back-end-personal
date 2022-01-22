from django import forms

class ClienteForm(forms.Form):
    nombres = forms.CharField(label='Nombres',max_length=200,required=True)
    apellidos = forms.CharField(label='Apellidos',max_length=200,required=True)
    email = forms.EmailField(required=True)
    direccion = forms.CharField(widget=forms.Textarea)
    telefono = forms.CharField(max_length=20,required=True)
    usuario = forms.CharField(max_length=20,required=True)
    password = forms.CharField(widget=forms.PasswordInput)