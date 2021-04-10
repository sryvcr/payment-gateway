import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pasarela_pagos.payments.business_logic.payments import (
    get_payment_by_id,
    create_payment
)
from pasarela_pagos.payments.serializers.payment import (
    PaymentSerializer,
    PaymentCreateSerializer
)
from pasarela_pagos.payments.utils.make_response import make_response


class PaymentGetByPkView(APIView):

    def get(self, request, uid: str):
        try:
            try:
                payment = get_payment_by_id(uid)
                serializer = PaymentSerializer(payment)
                response = make_response(status.HTTP_200_OK, serializer.data)
                return Response(status=status.HTTP_200_OK, data=response)
            except:
                response = make_response(status.HTTP_404_NOT_FOUND, {})
                return Response(status=status.HTTP_404_NOT_FOUND, data=response)
        except Exception as e:
            print('error:', e)
            response = make_response(status.HTTP_400_BAD_REQUEST, str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST, data=response)


class PaymentCreateOneView(APIView):

    def post(self, request):
        try:
            body = json.loads(request.body)
            payment = create_payment(
                value_after_iva=body['value_after_iva'],
                value_total=body['value_total'],
                iva=body['iva'],
                user_id=body['user_id'],
                payment_token=body['payment_token'],
                dues=body['dues'],
                payment_reference=body['payment_reference'],
                webhook_url=body['webhook_url']
            )
            serializer = PaymentCreateSerializer(payment)
            response = make_response(status.HTTP_201_CREATED, serializer.data)
            return Response(status=status.HTTP_201_CREATED, data=response)
        except Exception as e:
            print('error:', e)
            response = make_response(status.HTTP_400_BAD_REQUEST, str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST, data=response)