import pytest
from rest_framework.test import APIClient
from inventory_management.models import Product
from base.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    user = User.objects.create_user(
        email="testuser@example.com",
        first_name="Test",
        last_name="User",
        password="testpassword123"
    )
    return user


@pytest.fixture
def admin_user():
    user = User.objects.create_superuser(
        email="adminuser@example.com",
        first_name="Admin",
        last_name="User",
        password="adminpassword123"
    )
    return user


@pytest.fixture
def product(admin_user):
    return Product.objects.create(
        name="Sample Product",
        description="This is a sample product",
        quantity=10,
        price=100.00,
    )
