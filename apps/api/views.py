from django.shortcuts import get_object_or_404
from rest_framework import generics
from apps.api.models import Account, Transaction
from apps.api.serializers import AccountSerializer, TransactionSerializer

# Create your views here.
class AccountListCreate(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        self.queryset = Account.objects.filter(user=self.request.user)
        return super().get_queryset()

    def create(self, request, *args, **kwargs):
        request.data.update({'user': request.user.id})
        return super().create(request, *args, **kwargs)


class TransactionCreate(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def get_account(self):
        return get_object_or_404(
            Account, pk=self.kwargs['account'], user=self.request.user
        )

    def create(self, request, *args, **kwargs):
        account = self.get_account()
        request.data.update({'account': account.id})
        return super().create(request, *args, **kwargs)
