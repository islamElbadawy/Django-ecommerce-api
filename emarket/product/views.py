from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from .filters import ProductsFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from rest_framework.pagination import PageNumberPagination
# Create your views here.


@api_view(['GET'])
def get_all_products(request):
    filterSet = ProductsFilter(request.GET, queryset=Product.objects.all().order_by('id'))
    count = filterSet.qs.count();
    pageSize = request.GET.get('pageSize') or 1
    paginator = PageNumberPagination()
    paginator.page_size = pageSize

    queryset = paginator.paginate_queryset(filterSet.qs, request)
    serializer = ProductSerializer(queryset, many=True)
    return Response({"count": count, "per page": pageSize, "products": serializer.data })


@api_view(['GET'])
def get_product_by_id(request, pk):
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product(request):
    data = request.data
    print(data)
    serializer = ProductSerializer(data = data)
    if serializer.is_valid():
        product = Product.objects.create(**data, user = request.user)
        res = ProductSerializer(product, many=False)
        return Response(res.data)
    else:
        return Response(serializer.errors)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    
    if request.user != product.user:
        return Response({"error": "You can not update this product", "status": status.HTTP_403_FORBIDDEN})

    product.name = request.data['name']
    product.description = request.data['description']
    product.price = request.data['price']
    product.brand = request.data['brand']
    product.category = request.data['category']
    product.rating = request.data['rating']
    product.stock = request.data['stock']

    product.save()

    serializer = ProductSerializer(product, many=False);
    return Response({"message":"Product has been updated successfully", "product": serializer.data})



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_product(request, pk):
    product = get_object_or_404(Product, id=pk)
    
    if request.user != product.user:
        return Response({"error": "You can not delete this product", "status": status.HTTP_403_FORBIDDEN})

    product.delete()
    return Response({"message":"Product has been deleted successfully", "status": status.HTTP_200_OK})
