from rest_framework import serializers
from pasarela_pagos.payments.models import Payment, Repayment


class PaymentSerializer(serializers.ModelSerializer):
    uid = serializers.SerializerMethodField()
    value_after_iva = serializers.IntegerField()
    value_total = serializers.IntegerField()
    iva = serializers.IntegerField()
    status = serializers.CharField()
    user_id = serializers.CharField()
    payment_token = serializers.CharField()
    dues = serializers.IntegerField()
    payment_reference = serializers.CharField()
    webhook_url = serializers.CharField()
    created_date = serializers.DateTimeField()

    class Meta:
        model = Payment
        fields = (
            'uid',
            'value_after_iva',
            'value_total',
            'iva',
            'status',
            'user_id',
            'payment_token',
            'dues',
            'payment_reference',
            'webhook_url',
            'created_date'
        )
        read_only_fields = (
            'uid',
            'value_after_iva',
            'value_total',
            'iva',
            'status',
            'user_id',
            'payment_token',
            'dues',
            'payment_reference',
            'webhook_url',
            'created_date'
        )

    def get_uid(self, obj):
        return obj.id

class PaymentCreateSerializer(PaymentSerializer):
    uid = serializers.SerializerMethodField()
    status = serializers.CharField()
    created_date = serializers.DateTimeField()

    class Meta(PaymentSerializer.Meta):
        fields = (
            'uid',
            'status',
            'created_date'
        )
        read_only_fields = (
            'uid',
            'status',
            'created_date'
        )

    def get_uid(self, obj):
        return obj.id


class RepaymentSerializer(PaymentSerializer):
    repayments = serializers.SerializerMethodField()

    class Meta(PaymentSerializer.Meta):
        fields = PaymentSerializer.Meta.fields + (
            'repayments',
        )
        read_only_fields = PaymentSerializer.Meta.read_only_fields + (
            'repayments',
        )

    def get_uid(self, obj):
        return obj.id

    def get_repayments(self, obj):
        repayments = Repayment.objects.filter(payment_id=obj.id).all()
        return repayments.values()
