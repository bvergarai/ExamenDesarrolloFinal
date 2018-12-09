from django import forms
#Importamos el Modelo de Peros_Rescatados
from .models import RegistroCliente,OrdenTrabajo


#Crear el formulario de Perro Rescatad


class RegistroCliente_form(forms.ModelForm):
	class Meta:
		model=RegistroCliente
		fields=('Nombre_Completo','Direccion' , 'Ciudad' , 'Comuna','Correo', )	