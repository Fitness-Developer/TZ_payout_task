import time
import logging
from celery import shared_task
from django.db import transaction
from .models import Payout

logger = logging.getLogger(__name__)

@shared_task(bind=True, acks_late=True)
def process_payout_task(self, payout_id: int):
    """Простая имитация фоновой обработки заявки."""
    try:
        payout = Payout.objects.get(pk=payout_id)
    except Payout.DoesNotExist:
        logger.error("Payout %s not found", payout_id)
        return

    # Set to processing
    Payout.objects.filter(pk=payout_id).update(status=Payout.Status.PROCESSING)
    logger.info("Processing payout %s", payout_id)

    # Simulate some processing: validations, external call, etc
    time.sleep(2)  # имитация задержки; в реальном — вызов внешнего API

    # Простая проверка: если сумма слишком большая — fail, иначе complete
    if payout.amount > 10000:
        new_status = Payout.Status.FAILED
    else:
        new_status = Payout.Status.COMPLETED

    Payout.objects.filter(pk=payout_id).update(status=new_status)
    logger.info("Payout %s finished with status %s", payout_id, new_status)
    return {"payout_id": payout_id, "status": new_status}