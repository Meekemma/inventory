import pytest
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from inventory_management.models import Product

# Use the custom user model
User = get_user_model()


@pytest.fixture
def api_client():
    """Fixture to provide an unauthenticated API client."""
    return APIClient()


@pytest.fixture
def admin_user(db):
    """Fixture to create an admin user."""
    return User.objects.create_superuser(
        email="admin@example.com",
        first_name="Admin",
        last_name="User",
        password="adminpass123"
    )


@pytest.fixture
def authenticated_admin_client(admin_user):
    """Fixture to provide an authenticated API client for the admin user."""
    client = APIClient()
    client.force_authenticate(user=admin_user)
    return client


@pytest.fixture
def product_factory(db):
    """Fixture to create multiple products for testing."""
    def create_products(**kwargs):
        return Product.objects.create(**kwargs)
    return create_products


@pytest.fixture
def test_products(product_factory):
    """Fixture to create a batch of test products."""
    return Product.objects.bulk_create([
        Product(name="Product A", description="Low stock product", quantity=5, price=50.00),
        Product(name="Product B", description="In stock product", quantity=15, price=150.00),
        Product(name="Product C", description="Medium stock product", quantity=8, price=80.00),
    ])
