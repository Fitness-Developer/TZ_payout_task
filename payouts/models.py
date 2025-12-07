from django.db import models
from django.core.validators import MinValueValidator, RegexValidator

class Payout(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        PROCESSING = "processing", "Processing"
        COMPLETED = "completed", "Completed"
        FAILED = "failed", "Failed"
        CANCELLED = "cancelled", "Cancelled"

    amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.01)])
    currency = models.CharField(max_length=3, default="EUR")  # ISO 4217 code
    recipient_name = models.CharField(max_length=200)
    recipient_account = models.CharField(max_length=64, validators=[RegexValidator(r"^[A-Za-z0-9\-\s]+$")])
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    description = models.TextField(blank=True, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Payout {self.pk} {self.amount} {self.currency} to {self.recipient_name}"