from rest_framework import serializers
from pasarela_pagos.payments.models import User, UserCreditCard


class UserSerializer(serializers.ModelSerializer):
    uid = serializers.SerializerMethodField()
    fullname = serializers.DateTimeField()
    email = serializers.EmailField()
    created_date = serializers.DateTimeField()

    class Meta:
        model = User
        fields = (
            'uid',
            'fullname',
            'email',
            'created_date',
        )
        read_only_fields = (
            'uid',
            'fullname',
            'email',
            'created_date',
        )

    def get_uid(self, obj):
        return obj.id


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


class LinkCreditCardSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    created_date = serializers.DateTimeField()

    class Meta:
        model = UserCreditCard
        fields = (
            'token',
            'created_date',
        )
        read_only_fields = (
            'token',
            'created_date',
        )

    def get_token(self, obj):
        return obj.id
