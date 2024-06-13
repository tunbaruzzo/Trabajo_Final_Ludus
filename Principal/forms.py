from django import forms

class formulario_miembro(forms.Form):
        
    nombre = forms.CharField()
    apellido = forms.CharField()
    celular= forms.IntegerField()

class formularioinstructor(forms.Form):
        
    nombre = forms.CharField()
    apellido = forms.CharField()
    celular= forms.IntegerField()

class formularioprograma(forms.Form):
    CATEGORIA_OPCIONES =[
        ('Cardio', 'Cardio'),
        ('Fuerza', 'Fuerza'),
        ('Movimiento', 'Movimiento'),
        ('Flexibilidad', 'Flexibilidad'),
        ]
        
    nombre= forms.CharField()
    categoria= forms.ChoiceField(choices=CATEGORIA_OPCIONES)
    duracion= forms.IntegerField()
    capacidad= forms.IntegerField()