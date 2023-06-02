from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
# Create your views here.
def welcome(request):
    return HttpResponse(
        '<h1 style="background-color: brown;"> welcome </>'
    
    )

@api_view(['GET','POST'])
def todo_list_create(request):
    if request.method=='GET':
        todos=Todo.objects.all()
        serializer=TodoSerializer(todos,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def todo_get_update_delete(request,id):
    todo=get_object_or_404(Todo,pk=id)

    if request.method=='GET':        
        serializer=TodoSerializer(todo)
        return Response(serializer.data)
    
    elif request.method=='PUT':
        serializer=TodoSerializer(data=request.data,instance=todo)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method=='DELETE':
         todo.delete()
         return Response(status=status.HTTP_200_OK)   
    
######### CBV ###############
class Todos(ListCreateAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
    lookup_field=id

class TodosRUD(RetrieveUpdateDestroyAPIView):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer

###########
class TodoMVS(ModelViewSet):
    queryset=Todo.objects.all()
    serializer_class=TodoSerializer
