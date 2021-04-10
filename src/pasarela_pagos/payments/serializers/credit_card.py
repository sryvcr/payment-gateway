from rest_framework import serializers
from ..models import CreditCard


class CreditCardSerializer(serializers.ModelSerializer):
    uid = serializers.SerializerMethodField()
    card_number = serializers.CharField()
    franchise = serializers.CharField()
    due_date = serializers.CharField()
    created_date = serializers.DateTimeField()

    class Meta:
        model = CreditCard
        fields = (
            'uid',
            'card_number',
            'franchise',
            'due_date',
            'created_date',
        )
        read_only_fields = (
            'uid',
            'card_number',
            'franchise',
            'due_date',
            'created_date',
        )

    def get_uid(self, obj):
        return obj.id


class CreditCardCreateSerializer(serializers.ModelSerializer):
    uid = serializers.SerializerMethodField()
    franchise = serializers.CharField()
    first_six_numbers = serializers.SerializerMethodField()
    last_four_numbers = serializers.SerializerMethodField()
    due_date = serializers.CharField()
    created_date = serializers.DateTimeField()

    class Meta:
        model = CreditCard
        fields = (
            'uid',
            'franchise',
            'first_six_numbers',
            'last_four_numbers',
            'due_date',
            'created_date',
        )
        read_only_fields = (
            'uid',
            'franchise',
            'first_six_numbers',
            'last_four_numbers',
            'due_date',
            'created_date',
        )

    def get_uid(self, obj):
        return obj.id

    def get_first_six_numbers(self, obj):
        return str(obj.card_number)[0:6]

    def get_last_four_numbers(self, obj):
        return str(obj.card_number)[-4:]
