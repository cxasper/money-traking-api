from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class CustomJWTSerializer(JSONWebTokenSerializer):
    username_field = 'email'

    def validate(self, attrs):
        password = attrs.get('password')
        email = attrs.get('email')
        user_obj = User.objects.filter(email=email).first()
        if user_obj is not None:

            if not user_obj.is_active:
                msg = _('Unable to log in with account disable.')
                raise serializers.ValidationError(msg)

            credentials = { 'email': email, 'password': password}

            user = self.authenticate(**credentials)

            if user:

                payload = jwt_payload_handler(user)

                return {
                    'token': jwt_encode_handler(payload),
                    'user': user
                }
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)

        else:
            msg = _('Account with this email does not exist')
            raise serializers.ValidationError(msg)

    def authenticate(self, email=None, password=None):
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
                return None
