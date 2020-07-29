from rest_framework import generics
from apps.api.models import Account
from apps.api.serializers import AccountSerializer

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
