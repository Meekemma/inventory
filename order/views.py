from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import OrderSerializer
from .models import Order



# Create your views here.
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    serializer = OrderSerializer(data=request.data, context={'request': request})
    
    if serializer.is_valid(raise_exception=True):
        serializer.save(status='pending')
        return Response({'message': 'Order created successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)
    
    return Response({'message': 'Order creation failed', 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def track_status(request):
    """
    Filter orders based on their status and is_paid field.
    """

    # Get the query parameters provided for filtering
    order_status = request.query_params.get('status', None) 
    is_paid = request.query_params.get('is_paid', None)

    # Validate query parameters
    if not order_status or is_paid is None:
        return Response(
            {"error": "Both 'status' and 'is_paid' query parameters are required."},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        # Filter orders based on the provided status and is_paid values
        orders = Order.objects.filter(status=order_status, is_paid=is_paid)

        # Serialize the filtered orders
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    except Exception as e:
        # Catch unexpected errors and return an internal server error
        return Response(
            {"error": f"An error occurred: {str(e)}"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)




@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def status_update(request, order_id):
    """
    Admin users can update the status and payment status of an order.
    """
    # Fetch the order instance
    order = get_object_or_404(Order, id=order_id)

    # Update the order with the provided data
    serializer = OrderSerializer(order, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    # If the data is invalid, this will be raised automatically by `raise_exception=True`
    return Response({"error": "Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
