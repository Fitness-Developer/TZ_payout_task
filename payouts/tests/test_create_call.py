import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from unittest import mock

@pytest.mark.django_db
def test_celery_task_called_on_create(monkeypatch):
    client = APIClient()
    url = reverse("payout-list")
    payload = {
        "amount": "10.00",
        "currency": "USD",
        "recipient_name": "Bob",
        "recipient_account": "ACC12345"
    }


    with mock.patch("payouts.tasks.process_payout_task.delay") as mocked_delay:
        resp = client.post(url, payload, format="json")
        assert resp.status_code == 201
        assert mocked_delay.called
        args, kwargs = mocked_delay.call_args
        assert len(args) == 1