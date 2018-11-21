from django import forms
from .models import Gato

class GatoForm(forms.ModelForm):
 	class Meta:

 		model=Gato
 		
 		fields=['nombre','raza','genero','edad']

 		label={"nombre":"Nombre:","raza":"Raza:","genero":"Genero:",'edad':'Edad:'}

 		widgets={"nombre":forms.TextInput(attrs={'class':'form-control'}),
 		"raza":forms.TextInput(attrs={'class':'form-control'}),
 		"genero":forms.TextInput(attrs={'class':'form-control'}),
 		"edad":forms.TextInput(attrs={'class':'form-control'}),
 		}


