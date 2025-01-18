import pytest
from rest_framework import status
from inventory_management.models import Product


@pytest.mark.django_db
def test_product_view(api_client, user, product):
    url = '/inventory_management/products/'

    # Authenticate as regular user
    api_client.force_authenticate(user=user)

    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert 'results' in response.data  # Ensure pagination works and results key exists
    assert len(response.data['results']) > 0  # There should be at least one product


@pytest.mark.django_db
def test_product_detail(api_client, user, product):
    url = f'/inventory_management/products/{product.id}/'

    # Authenticate as regular user
    api_client.force_authenticate(user=user)

    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == product.name
    assert response.data['description'] == product.description


@pytest.mark.django_db
def test_create_product(api_client, admin_user):
    url = '/inventory_management/products/create/'

    # Authenticate as admin user
    api_client.force_authenticate(user=admin_user)

    data = {
        "name": "New Product",
        "description": "Description of the new product",
        "quantity": 50,
        "price": 150.00
    }

    response = api_client.post(url, data, format="json")
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data['name'] == data['name']
    assert response.data['description'] == data['description']


@pytest.mark.django_db
def test_update_product(api_client, admin_user, product):
    url = f'/inventory_management/products/update/{product.id}/'

    # Authenticate as admin user
    api_client.force_authenticate(user=admin_user)

    data = {
        "name": "Updated Product",
        "description": "Updated description",
        "quantity": 20,
        "price": 120.00
    }

    response = api_client.put(url, data, format="json")
    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == data['name']
    assert response.data['description'] == data['description']


@pytest.mark.django_db
def test_delete_product(api_client, admin_user, product):
    url = f'/inventory_management/products/delete/{product.id}/'

    # Authenticate as admin user
    api_client.force_authenticate(user=admin_user)

    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert Product.objects.count() == 0  # Ensure the product is deleted


@pytest.mark.django_db
def test_product_view_no_permission(api_client, user):
    url = '/inventory_management/products/'

    # Authenticate as a regular user (not an admin)
    api_client.force_authenticate(user=user)

    response = api_client.post(url, data={}, format="json") 
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
