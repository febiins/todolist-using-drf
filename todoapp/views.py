from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from.serializers import TodoSerializer
from .models import Todo


# Create your views here.

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])

def todo_list(request):
    if request.method == 'GET':
        todos=Todo.objects.all()
        print(todos)
        serializer=TodoSerializer(todos,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])

def todo_detail(request,pk):
   try:
      todo=Todo.objects.get(pk=pk)
   except Exception as e:
      return Response ({'error':'Not found'},status=status.HTTP_404_NOT_FOUND)
   
   if request.method=='GET':
       serializers=TodoSerializer(todo)
       return Response(serializers.data)
   elif request.method=='PUT':
       serializers=TodoSerializer(todo,data=request.data)
       if serializers.is_valid():
           serializers.save()
           return Response(serializers.data)
       return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
   elif request.method=='DELETE':
       todo.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
       
        

    
