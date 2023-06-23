from django.shortcuts import render, redirect
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Serializer
from .models import Model

# Create your views here.
def index(request):
    return redirect('documentation/')
@api_view(['POST'])
def Add(request):
    serializer = Serializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'status':'data telah ditambahkan',
            'id':serializer.data['id'],
            'nama cabang':serializer.data['nama_cabang'],
            'deskripsi':serializer.data['deskripsi'],
            'sejarah':serializer.data['sejarah'],
        })
    return Response(serializer.errors)
@api_view(['GET'])
def List(request):
    ModelObject=Model.objects.all()
    SerializerObject = Serializer(ModelObject,many=True)
    return Response(SerializerObject.data)
@api_view(['PUT'])
def Update(request, id):
    try:
        ModelObject = Model.objects.get(id=id)
    except Model.DoesNotExist:
        status = {'status':'data tidak ditemukan'}
        return Response(status)
    serializer = Serializer(ModelObject, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def Delete(request, id):
    try:
        ModelObject = Model.objects.get(id=id)
    except Model.DoesNotExist:
        status = {'status':'data tidak ditemukan'}
        return Response(status)
    ModelObject.delete()
    return Response({
        'status':'data telah dihapus'
    })