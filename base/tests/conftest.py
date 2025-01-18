import pytest
from rest_framework.test import APIClient
from base.models import User


@pytest.fixture
def api_client():
    """Provides a reusable APIClient instance."""
    return APIClient()


@pytest.fixture
def user(db):
    """Creates a test user."""
    return User.objects.create_user(
        email="paul123peeter@gmail.com", 
        first_name="Paul",
        last_name="Peter",
        password="paulpeter123"  
    )


@pytest.fixture
def user_payload():
    """Provides a sample user payload."""
    return {
        "first_name": "Emmanuel",
        "last_name": "Ibeh",
        "email": "Ibehemmanuel32@gmail.com",
        "password": "Iloveemma",
        "password2": "Iloveemma",
    }


@pytest.fixture
def login_payload(user) -> dict:
    return{
        "email": user.email,
        "password": "paulpeter123"
    }
