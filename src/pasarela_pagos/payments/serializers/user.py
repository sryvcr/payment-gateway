from rest_framework import serializers
from pasarela_pagos.payments.models import User


class UserCreateSerializer(serializers.ModelSerializer):
    uid = serializers.SerializerMethodField()
    created_date = serializers.DateTimeField()

    class Meta:
        model = User
        fields = (
            'uid',
            'created_date',
        )
        read_only_fields = (
            'uid',
            'created_date',
        )

    def get_uid(self, obj):
        return obj.id
