from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Product
from .serializers import ProductSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def product_view(request):
    """
    List all products with pagination.
    """
    products = Product.objects.all()
    paginator = LimitOffsetPagination()
    paginated_products = paginator.paginate_queryset(products, request)
    serializer = ProductSerializer(paginated_products, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
@permission_classes([AllowAny])
def product_detail(request, pk):
    """
    Retrieve a single product by ID.
    """
    product = get_object_or_404(Product, id=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated, IsAdminUser])
def create_product(request):
    """
    Create a new product (admin only).
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'PATCH'])
@permission_classes([IsAuthenticated, IsAdminUser])
def update_product(request, pk):
    """
    Update an existing product by ID (admin only).
    Handles both PUT (full update) and PATCH (partial update).
    """
    product = get_object_or_404(Product, id=pk)
    
    # Determine if the request is a PATCH request or PUT request
    partial = request.method == 'PATCH'
    
    # Validate the data
    serializer = ProductSerializer(product, data=request.data, partial=partial)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # If validation fails, return errors
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
@permission_classes([IsAuthenticated, IsAdminUser])
def delete_product(request, pk):
    """
    Delete a product by ID (admin only).
    """
    product = get_object_or_404(Product, id=pk)
    product.delete()
    return Response(
        {'message': f'Product "{product.name}" deleted successfully.'},
        status=status.HTTP_204_NO_CONTENT
    )
