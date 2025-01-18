import pytest
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken
from datetime import timedelta
from django.utils.timezone import now

import logging

logger = logging.getLogger(__name__)

@pytest.mark.django_db
def test_user_creation(api_client, user_payload):
    """
    Test user registration endpoint.
    """
    url = '/base/registration/' 

    # Sending a POST request to the registration endpoint
    response_create = api_client.post(url, data=user_payload, format="json")
    
    logger.info(f"Create Response Data: {response_create.data}")

    # Asserting the response status and message
    assert response_create.status_code == 201
    assert response_create.data['message'] == 'User created successfully'

    

    




@pytest.mark.django_db
def test_user_login(api_client, login_payload) -> None:
    url = '/base/login/'  # Replace with your actual login URL

    # Send POST request to login endpoint
    response_login = api_client.post(url, data=login_payload, format="json")
    
    logger.info(f"Login Response Data: {response_login.data}")

    # Check the status code
    assert response_login.status_code == 200

    # Validate that the response contains JWT tokens
    assert 'access' in response_login.data
    assert 'refresh' in response_login.data




