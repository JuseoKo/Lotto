from tables.models.service.user import User
from tables.models.service.lotto_user import LottoAccount
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'phone_number', 'nickname']

class LottoAccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LottoAccount
        fields = ['user_id', 'lotto_id', 'lotto_password']
