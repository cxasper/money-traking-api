from django.urls import path
from rest_framework_jwt.views import ObtainJSONWebToken
from apps.api.serializers import CustomJWTSerializer
from apps.api.views import AccountListCreate, TransactionCreate, \
    AccountDetail


obtain_jwt_token = ObtainJSONWebToken.as_view(
    serializer_class=CustomJWTSerializer
)


urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
    path('accounts/', AccountListCreate.as_view(), name='list-accounts'),
    path(
        'accounts/<int:pk>/', AccountDetail.as_view(),
        name='detail-accounts'
    ),
    path(
        'accounts/<int:account>/transactions/', TransactionCreate.as_view()
    ),
]
