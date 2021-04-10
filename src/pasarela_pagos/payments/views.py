import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pasarela_pagos.payments.business_logic.credit_cards import create_credit_card
from pasarela_pagos.payments.serializers.credit_card import CreditCardCreateSerializer
from pasarela_pagos.payments.utils.make_response import make_response


class CreditCardCreateOneView(APIView):

    def post(self, request):
        try:
            body = json.loads(request.body)
            credit_card = create_credit_card(
                card_number=body['card_number'],
                due_date=body['due_date']
            )
            serializer = CreditCardCreateSerializer(credit_card)
            response = make_response(status.HTTP_201_CREATED, serializer.data)
            return Response(status=status.HTTP_201_CREATED, data=response)
        except Exception as e:
            print('error:', e)
            response = make_response(status.HTTP_400_BAD_REQUEST, str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST, data=response)
