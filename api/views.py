from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from api.models import Stay
from api.serializers import StaySerializer


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
