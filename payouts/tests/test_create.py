import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from payouts.models import Payout

@pytest.mark.django_db
def test_create_payout_success():
    client = APIClient()
    url = reverse("payout-list")
    payload = {
        "amount": "123.45",
        "currency": "EUR",
        "recipient_name": "Alice",
        "recipient_account": "DE89 3704 0044 0532 0130 00",
        "description": "Test payout"
    }
    resp = client.post(url, payload, format="json")
    assert resp.status_code == 201, resp.content
    data = resp.json()
    assert data["amount"] == "123.45"
    assert data["currency"] == "EUR"
    assert Payout.objects.filter(pk=data["id"]).exists()