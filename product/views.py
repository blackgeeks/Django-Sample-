from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from product.models import Product
from product.serializers import ProductSerialzer

ITEMS_PER_PAGE = 12


class ProductManagement(APIView):
    def get(self, request, *args, **kwargs):
        try:
            products = Product.objects.all()
            paginator = Paginator(products, ITEMS_PER_PAGE)
            page = request.GET.get('page')
            try:
                product_list = paginator.page(page)
            except PageNotAnInteger:
                product_list = paginator.page(1)
            except EmptyPage:
                product_list = paginator.page(paginator.num_pages)

            product_serializer = ProductSerialzer(product_list, many=True)
            return Response({"data": product_serializer.data,
                             "totalRecords": paginator.count,
                             "recordsPerPage": ITEMS_PER_PAGE,
                             "totalPages": paginator.num_pages,
                             "page": page, },
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"msg": "Something went wrong", "error": str(e)},
                            status=status.HTTP_409_CONFLICT)
