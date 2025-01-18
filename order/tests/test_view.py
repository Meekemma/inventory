import pytest
from rest_framework.reverse import reverse
from order.models import Order, OrderItem


@pytest.mark.django_db
def test_create_order(api_client, normal_user, product):
    api_client.force_authenticate(user=normal_user)
    url = '/order/create-order/'
    payload = {
        "order_items": [
            {"product": product.id, "quantity": 2}
        ]
    }
    response = api_client.post(url, data=payload, format="json")

    assert response.status_code == 201
    assert response.data["message"] == "Order created successfully"
    assert Order.objects.filter(user=normal_user).count() == 1



@pytest.mark.django_db
def test_track_status(api_client, admin_user, create_orders):
    api_client.force_authenticate(user=admin_user)
    url = '/order/track_status/?status=pending&is_paid=False'

    response = api_client.get(url)

    assert response.status_code == 200
    assert len(response.data) == 3  # Assuming the `create_orders` fixture creates 3 orders



@pytest.mark.django_db
def test_status_update(api_client, admin_user, create_orders):
    api_client.force_authenticate(user=admin_user)
    order = create_orders[0]
    url = f'/order/status_update/{order.id}/'

    payload = {"status": "completed", "is_paid": True}
    response = api_client.put(url, data=payload, format="json")

    assert response.status_code == 200
    assert response.data["status"] == "completed"
    assert response.data["is_paid"] is True


