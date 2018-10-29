from django import forms
from .models import Software,Departamento

class SoftwareForm(forms.ModelForm):
 	class Meta:

 		model=Software
 		
 		fields=['nombre','funcion','departamento']

 		label={"nombre":"Nombre","categoria":"Categoria","departamento":"Departamento"}

 		widgets={"nombre":forms.TextInput(attrs={'class':'form-control'}),"funcion":forms.TextInput(attrs={'class':'form-control'}),"departamento":forms.Select(attrs={'class':'form-control'})}





class DepartamentoForm(forms.ModelForm):
 	class Meta:

 		model=Departamento
 		
 		fields=['nombre']

 		label={"nombre":"Nombre"}

 		widgets={"nombre":forms.TextInput(attrs={'class':'form-control'})}