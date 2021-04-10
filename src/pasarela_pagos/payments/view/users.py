import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pasarela_pagos.payments.business_logic.users import (
    create_user
)
from pasarela_pagos.payments.serializers.user import (
    UserCreateSerializer
)
from pasarela_pagos.payments.utils.make_response import make_response


class UserCreateOneView(APIView):

    def post(self, request):
        try:
            body = json.loads(request.body)
            user = create_user(
                fullname=body['fullname'],
                email=body['email']
            )
            serializer = UserCreateSerializer(user)
            response = make_response(status.HTTP_201_CREATED, serializer.data)
            return Response(status=status.HTTP_201_CREATED, data=response)
        except Exception as e:
            print('error:', e)
            response = make_response(status.HTTP_400_BAD_REQUEST, str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST, data=response)
