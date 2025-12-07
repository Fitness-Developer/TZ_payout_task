from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Payout
from .serializers import PayoutSerializer
from .tasks import process_payout_task

class PayoutViewSet(viewsets.ModelViewSet):
    queryset = Payout.objects.all()
    serializer_class = PayoutSerializer

    def perform_create(self, serializer):
        payout = serializer.save()
        process_payout_task.delay(payout.id)
