from rest_framework import serializers
from api.models import BankAccount


class BankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        models = BankAccount
        fields = '__all__'