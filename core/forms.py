from django import forms
from django.db.models import fields
from django.forms import ModelForm,widgets
from .models import Usuario


class Name(ModelForm):
    class Meta:
        model=Usuario
        fields=[
            'NombreCompleto', 
            'Telefono',
            'Rut',
            'Pais',
            'correo',
            'foto',
            'Direccion',


        ]
        widgets={
            'NombreCompleto':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'name':'nombre',
                    'placeholder':'Escribe Tu Nombre Completo'

                }
            ),
            'Telefono':forms.NumberInput(
                attrs={
                    'class':'form-control',
                    'name':'numero',
                    'placeholder':'Anota tu numero'
                }
            ),
            'Rut':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'name':'Run',
                    'placeholder':'Ingrese su rut'
                }
            ),
            'Pais':forms.Select(
                attrs={
                    'class':'form-control',
                    'id':'Pais',
                }
            ),
            'correo':forms.EmailInput(
                attrs={
                    'class':'form-control',
                    'name':'correo',
                    'placeholder':'Ingrese su E-mail'
                }
            ),
            'foto':forms.FileInput(

            ),
            'Direccion':forms.TextInput(
                attrs={
                    'class':'form-control',
                    'name':'Direccion',
                    'placeholder':'Ingrese su direccion'
                }
            ),
            
                
            }




        

