from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from api.models import Stay, Cafe, Res, CafeTag, ResTag
from api.serializers import StaySerializer, CafeSerializer, ResSerializer
from api.serializers import CafeTagSerializer, ResTagSerializer


# cafe
@api_view(['GET'])
def get_all_cafe(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    data = Cafe.objects.all().order_by('-review_count')[:30]
    result_page = paginator.paginate_queryset(data, request)
    serializer = CafeSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
# stay
@api_view(['GET'])
def get_filter_stay(request):
    paginator = PageNumberPagination()
    paginator.page_size = 10
    params = request.query_params
    district = params['district']
    data = Stay.objects.filter(district=district)
    result_page = paginator.paginate_queryset(data, request)
    serializer = StaySerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
