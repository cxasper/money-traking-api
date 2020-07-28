from django.urls import path
from rest_framework_jwt.views import ObtainJSONWebToken
from apps.api.serializers import CustomJWTSerializer


obtain_jwt_token = ObtainJSONWebToken.as_view(
    serializer_class=CustomJWTSerializer
)


urlpatterns = [
    path('login/', obtain_jwt_token, name='login'),
]
