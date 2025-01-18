import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from inventory_management.models import Product

# Use the custom user model
User = get_user_model()


@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def admin_user():
    return User.objects.create_superuser(
        email="admin@example.com",
        first_name="Admin",
        last_name="User",
        password="adminpass123"
    )

@pytest.fixture
def normal_user():
    return User.objects.create_user(
        email="user@example.com",
        first_name="User",
        last_name="Normal",
        password="userpass123"
    )

@pytest.fixture
def product():
    return Product.objects.create(
        name="Test Product",
        description="This is a test product.",
        quantity=20,
        price=100.0
    )
