from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# ------------------------------
# Wallet model
# ------------------------------
class Wallet(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='wallet')
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)  # Optional but recommended

    def __str__(self):
        return f"{self.user.username}'s Wallet"

    # Method to spend funds
    def spend(self, amount, reference, description=''):
        if self.balance < amount:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.save()
        WalletTransaction.objects.create(
            wallet=self,
            transaction_type='SPEND',
            amount=amount,
            reference=reference,
            description=description
        )

    # Method to top-up funds
    def topup(self, amount, reference, description=''):
        self.balance += amount
        self.save()
        WalletTransaction.objects.create(
            wallet=self,
            transaction_type='TOPUP',
            amount=amount,
            reference=reference,
            description=description
        )

# ------------------------------
# WalletTransaction model
# ------------------------------
class WalletTransaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('TOPUP', 'Top-up'),
        ('SPEND', 'Spend'),
        ('WITHDRAW', 'Withdraw'),
    ]

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    reference = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.transaction_type} - {self.amount} UGX"

# ------------------------------
# WithdrawalRequest model
# ------------------------------
class WithdrawalRequest(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('APPROVED', 'Approved'),
        ('DECLINED', 'Declined'),
    ]

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.wallet.user.username} - {self.amount} UGX ({self.status})"