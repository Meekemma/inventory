import pytest
from rest_framework import status
from inventory_management.models import Product


@pytest.mark.django_db
def test_stock_report_default_threshold(authenticated_admin_client, test_products):
    """Test stock report with the default threshold (10)."""
    url = "/report/stock_report/"
    response = authenticated_admin_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2  # Products below the default threshold


@pytest.mark.django_db
def test_stock_report_custom_threshold(authenticated_admin_client, test_products):
    """Test stock report with a custom threshold."""
    url = "/report/stock_report/?threshold=15"
    response = authenticated_admin_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 2  # Only products below the custom threshold
    product_names = [product["name"] for product in response.data]
    assert "Product A" in product_names
    assert "Product C" in product_names
    assert "Product B" not in product_names


   


@pytest.mark.django_db
def test_sales_report_invalid_period(authenticated_admin_client):
    """Test sales report with an invalid period."""
    url = "/report/sales_report/?period=invalid"
    response = authenticated_admin_client.get(url)

    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "Invalid period" in response.data["error"]
