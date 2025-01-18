import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from inventory_management.models import Product
from order.models import Order

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
        first_name="Normal",
        last_name="User",
        password="userpass123"
    )


@pytest.fixture
def product():
    return Product.objects.create(
        name="Sample Product",
        description="A sample product description",
        quantity=100,
        price=50.00
    )


@pytest.fixture
def create_orders(product, normal_user):
    orders = [
        Order.objects.create(
            user=normal_user,                # Assign the order to the provided user
            status="pending",                # Set the order status to "pending"
            is_paid=False,                   # Mark the order as unpaid
            total_price=product.price        # Use the price of the provided product as the total price
        ) for _ in range(3)                  # Repeat this process 3 times
    ]
    return orders
