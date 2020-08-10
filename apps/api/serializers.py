from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from rest_framework_jwt.settings import api_settings
from apps.api.models import Account, Transaction


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


class AccountSerializer(serializers.ModelSerializer):
    currency_code = serializers.CharField(
        source='currency.code', read_only=True)
    currency_country = serializers.CharField(
        source='currency.country', read_only=True)

    class Meta:
        model = Account
        fields = '__all__'


class AccountDetailSerializer(AccountSerializer):
    transactions = serializers.SerializerMethodField()

    def get_transactions(self, instance):
        transactions = instance.transactions.all()
        serializer = TransactionSerializer(transactions, many=True)
        return serializer.data


class TransactionSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(
        source='type.name', read_only=True)
    type_color = serializers.CharField(
        source='type.theme_color', read_only=True)
    type_display_name = serializers.CharField(
        source='type.display_name', read_only=True)

    class Meta:
        model = Transaction
        fields = '__all__'
