from rest_framework import serializers
from .models import Persona, Tarea

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona 
        exclude = ['is_removed', 'created', 'modified']

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea  
        exclude = ['is_removed', 'created', 'modified']