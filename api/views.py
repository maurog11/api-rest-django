from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import Persona, Tarea
from .serializers import PersonaSerializer, TareaSerializer

class PersonListView(
  APIView,
  UpdateModelMixin, 
  DestroyModelMixin,
):

    def get(self):
        queryset = Persona.objects.all()
        read_serializer = PersonaSerializer(queryset, many=True)
    
        return Response(read_serializer.data)

    def post(self, request):
        create_serializer = PersonaSerializer(data=request.data)

        if create_serializer.is_valid():
            person_object = create_serializer.save()
            read_serializer = PersonaSerializer(person_object)

            return Response(read_serializer.data, status=201)

        return Response(create_serializer.errors, status=400)
    
    def put(self, request, id=None):
        try:
            person = Persona.objects.get(id=id)
        except Persona.DoesNotExist:
    
            return Response({'errors': 'No existe la persona'}, status=400)

        update_serializer = PersonaSerializer(person, data=request.data)

        if update_serializer.is_valid():
            person_object = update_serializer.save()
            read_serializer = PersonaSerializer(person_object)

            return Response(read_serializer.data, status=200)

        return Response(update_serializer.errors, status=400)

    def delete(self, id=None):
        try:
            persona = Persona.objects.get(id=id)
        except Persona.DoesNotExist:
       
            return Response({'errors': 'No existe la persona'}, status=400)

        persona.delete()

        return Response(status=204) 
    
class TaskListView(
  APIView,
  UpdateModelMixin, 
  DestroyModelMixin,
):
    
    def get(self):
        queryset = Tarea.objects.all()
        read_serializer = TareaSerializer(queryset, many=True)
    
        return Response(read_serializer.data)

    def post(self, request):
        create_serializer = TareaSerializer(data=request.data)

        if create_serializer.is_valid():
            task_object = create_serializer.save()
            read_serializer = TareaSerializer(task_object)

            return Response(read_serializer.data, status=201)

        return Response(create_serializer.errors, status=400)
    
    def put(self, request, id=None):
        try:
            task = Tarea.objects.get(id=id)
        except Tarea.DoesNotExist:
    
            return Response({'errors': 'No existe la tarea'}, status=400)

        update_serializer = TareaSerializer(task, data=request.data)

        if update_serializer.is_valid():
            task_object = update_serializer.save()
            read_serializer = TareaSerializer(task_object)

            return Response(read_serializer.data, status=200)

        return Response(update_serializer.errors, status=400)

    def delete(self, id=None):
        try:
            tarea = Tarea.objects.get(id=id)
        except Tarea.DoesNotExist:
       
            return Response({'errors': 'No existe la tarea'}, status=400)

        tarea.delete()

        return Response(status=204) 



