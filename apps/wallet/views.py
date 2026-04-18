from rest_framework import viewsets, permissions
from .models import Wallet, WalletTransaction
from .serializers import WalletSerializer, WalletTransactionSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

class WalletViewSet(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Wallet.objects.filter(user=self.request.user)

class WalletTransactionViewSet(viewsets.ModelViewSet):
    queryset = WalletTransaction.objects.all()
    serializer_class = WalletTransactionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return WalletTransaction.objects.filter(wallet__user=self.request.user)


class WalletViewSet(viewsets.ModelViewSet):
    ...

    @action(detail=False, methods=['post'])
    def topup(self, request):
        wallet = Wallet.objects.get(user=request.user)
        amount = request.data.get('amount')
        reference = request.data.get('reference')

        if not amount or not reference:
            return Response({'error': 'Amount and reference required.'}, status=status.HTTP_400_BAD_REQUEST)

        transaction = WalletTransaction.objects.create(
            wallet=wallet,
            transaction_type='TOPUP',
            amount=amount,
            reference=reference,
            description='Top-up via mock gateway'
        )
        wallet.balance += float(amount)
        wallet.save()

        return Response({'message': 'Wallet topped up successfully.', 'balance': wallet.balance})