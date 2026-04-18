from django.contrib import admin, messages
from django.db import transaction as db_transaction
from .models import Wallet, WalletTransaction

class TransactionInline(admin.TabularInline):
    model = WalletTransaction
    extra = 0
    readonly_fields = ('amount', 'transaction_type', 'timestamp')
    can_delete = False

@admin.action(description="Credit 1000 UGX to selected wallets")
def credit_wallets(modeladmin, request, queryset):
    with db_transaction.atomic():
        for wallet in queryset:
            wallet.balance += 1000
            wallet.save()
            WalletTransaction.objects.create(
                wallet=wallet,
                amount=1000,
                transaction_type='TOPUP',
                description='Admin adjustment',
                reference=f'ADMIN-{wallet.id}-{wallet.balance}'
            )
    modeladmin.message_user(request, "Wallets credited successfully.", messages.SUCCESS)

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance', 'updated_at')
    search_fields = ('user__username', 'user__email')
    readonly_fields = ('balance', 'created_at', 'updated_at')
    inlines = [TransactionInline]
    actions = [credit_wallets]

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_module_permission(self, request):
        return request.user.is_superuser