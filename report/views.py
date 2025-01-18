from rest_framework import status
from django.db.models import Sum, Count, DateField
from django.db.models.functions import TruncDay, TruncWeek, TruncMonth
from django.utils.timezone import now
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from inventory_management.models import Product
from inventory_management.serializers import ProductSerializer
from .utils import get_sales_data

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def stock_report(request):
    """
    Generate a report of products that are low in stock.
    Allows the admin to specify a threshold dynamically via query parameter.
    Default threshold is 10 if not specified.
    """
    # Get the threshold from query params or set default to 10
    threshold = request.query_params.get('threshold', 10)
    
    try:
        # Convert threshold to an integer
        threshold = int(threshold)
    except ValueError:
        return Response(
            {"error": "Threshold must be a valid integer."},
            status=status.HTTP_400_BAD_REQUEST
        )

    # Filter products based on the dynamic threshold
    low_stock_products = Product.objects.filter(quantity__lt=threshold)

    if not low_stock_products.exists():
        # Return a response indicating no products match the condition
        return Response(
            {"message": f"No products found with quantity less than {threshold}."},
            status=status.HTTP_200_OK
        )

    # Serialize and return the data
    serializer = ProductSerializer(low_stock_products, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)







@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUser])
def sales_report(request):
    """
    Generate a sales report based on the specified period (day, week, month) or date range.
    """
    period = request.query_params.get('period', None)
    start_date = request.query_params.get('start_date', None)
    end_date = request.query_params.get('end_date', None)

    try:
        # Call the helper function to get sales data
        data = get_sales_data(period=period, start_date=start_date, end_date=end_date)
    except ValueError as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # Handle empty data scenario
    if not data:
        return Response(
            {"message": "No sales data available for the specified period or range."},
            status=status.HTTP_200_OK,
        )

    return Response(data, status=status.HTTP_200_OK)
