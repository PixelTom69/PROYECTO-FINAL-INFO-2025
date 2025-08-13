from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre_completo', 'email', 'asunto', 'mensaje']
        widgets = {
            'nombre_completo': forms.TextInput(attrs={
                'placeholder': 'Nombre completo',
                'class': 'form-control',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'form-control',
                'required': True
            }),
            'asunto': forms.TextInput(attrs={
                'placeholder': 'Asunto',
                'class': 'form-control',
                'required': True
            }),
            'mensaje': forms.Textarea(attrs={
                'placeholder': 'Mensaje',
                'rows': 5,
                'class': 'form-control',
                'required': True
            }),
        }