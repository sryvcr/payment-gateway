from rest_framework import serializers
from pasarela_pagos.payments.models import Payment


class PaymentCreateSerializer(serializers.ModelSerializer):
    uid = serializers.SerializerMethodField()
    status = serializers.CharField()
    created_date = serializers.DateTimeField()

    class Meta:
        model = Payment
        fields = (
            'uid',
            'status',
            'created_date',
        )
        read_only_fields = (
            'uid',
            'status',
            'created_date',
        )

    def get_uid(self, obj):
        return obj.id