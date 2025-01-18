import pytest
from rest_framework import status
from django.urls import reverse
from inventory_management.models import Product
from base.models import User  # assuming custom user model

@pytest.mark.django_db
def test_stock_report_for_admin(client, admin_user, product):
    url = f'/report/stock_report/?threshold=10'
    client.force_login(admin_user)  # Log in as admin
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1  # Assuming the product has quantity less than threshold


@pytest.mark.django_db
def test_stock_report_no_products(client, admin_user):
    url = f'/report/stock_report/?threshold=1000'  # Assuming no product has this low quantity
    client.force_login(admin_user)
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert 'No products found' in response.data['message']


@pytest.mark.django_db
def test_sales_report_for_admin(client, admin_user):
    url = f'/report/sales_report/?period=day'
    client.force_login(admin_user)
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert isinstance(response.data, list)


@pytest.mark.django_db
def test_sales_report_invalid_period(client, admin_user):
    url = f'/report/sales_report/?period=invalid'
    client.force_login(admin_user)
    response = client.get(url)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert 'error' in response.data


@pytest.mark.django_db
def test_sales_report_no_data(client, admin_user):
    url = f'/report/sales_report/?period=month'
    client.force_login(admin_user)
    response = client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert 'No sales data available' in response.data['message']
