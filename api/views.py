from urllib import request
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from api.models import Livro
from api.serializer import LivroSerializer
# Create your views here.

@api_view(['GET'])
def getLivros(request):
    if request.method == 'GET':
        livros = Livro.objects.all()
        livros_serializer = LivroSerializer(livros, many=True)
        return Response(livros_serializer.data)

@api_view(['POST'])
def postLivro(request):
    if request.method == 'POST':
        livros_serializers = LivroSerializer(data=request.data)
        if livros_serializers.is_valid():
            livros_serializers.save()
            return Response(livros_serializers.data, status=status.HTTP_201_CREATED)
        else:
            return Response(livros_serializers.errors, status=status.HTTP_400_BAD_REQUEST)