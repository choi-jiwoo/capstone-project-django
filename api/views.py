from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import SampleCategory, SampleStoreList
from api.serializers import DataSerializer, StoreSerializer


# Create your views here.
@api_view(['GET'])
def get_cat(request):
    data = SampleCategory.objects.all()
    serializer = DataSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_filter_cat(request):
    params = request.query_params
    cat = params['cat']
    data = SampleCategory.objects.filter(category=cat)
    serializer = DataSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_store(request):
    data = SampleStoreList.objects.all()
    serializer = StoreSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_filter_store(request):
    params = request.query_params
    cat = params['cat']
    data = SampleStoreList.objects.filter(category=cat)
    serializer = StoreSerializer(data, many=True)
    return Response(serializer.data)
