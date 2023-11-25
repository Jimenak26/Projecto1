from django import forms
from django.forms import ModelForm, EmailInput, DateInput
from clientes.models import Cliente, Producto


class ClienteFormulario(ModelForm):
    tipo_producto = forms.ModelChoiceField(queryset=Producto.objects.all(), empty_label=None)

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'direccion', 'fecha_nacimiento', 'tipo_producto',
                  'activo']

        widgets = {'email': EmailInput(attrs={'type': 'email'}),
                   'fecha_nacimiento': DateInput(attrs={'type': 'date'})}
