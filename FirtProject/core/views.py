from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import create_new_block
from .models import Block
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from pprint import pprint



@api_view(['GET','POST'])
def get_chain(request):
    if request.method =='GET':
        chain = Block.objects.all()
        serializer = BlockModelSerializers(chain,many = True)
        return Response(data = {'blocks':serializer.data},status=status.HTTP_200_OK)

    if request.method == 'POST':
        serializer = BlockModelSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data = {'message':'created','data':serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response(data = {'errors':serializer.errors})



