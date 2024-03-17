from rest_framework import serializers
from tables.models.service.lotto_user import LottoAccount
from tables.models.service.user import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    phone_number = serializers.CharField(required=False)

    class Meta:
        model = User
        fields = ["user_id", "email", "nickname", "phone_number", "password"]


class LottoAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LottoAccount
        fields = ["user_id", "lotto_id", "lotto_password"]
