from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Serializer
from .models import Model

# Create your views here.
def index(request):
    return redirect('list/')
@api_view(['POST'])
def Add(request):
    serializer = Serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({
        'status':'data telah ditambahkan',
        'id':serializer.data['id'],
        'nama cabang':serializer.data['nama_cabang'],
        'deskripsi':serializer.data['deskripsi'],
        'sejarah':serializer.data['sejarah'],
    })
@api_view(['GET'])
def List(request):
    ModelObject=Model.objects.all()
    SerializerObject = Serializer(ModelObject,many=True)
    return Response(SerializerObject.data)