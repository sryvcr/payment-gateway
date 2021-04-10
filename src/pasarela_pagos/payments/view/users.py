import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pasarela_pagos.payments.business_logic.users import (
    get_user_by_id,
    create_user
)
from pasarela_pagos.payments.serializers.user import (
    UserSerializer,
    UserCreateSerializer
)
from pasarela_pagos.payments.utils.make_response import make_response


class UserGetByPk(APIView):

    def get(self, request, uid: str):
        try:
            try:
                user = get_user_by_id(uid)
                serializer = UserSerializer(user)
                response = make_response(status.HTTP_200_OK, serializer.data)
                return Response(status=status.HTTP_200_OK, data=response)
            except:
                response = make_response(status.HTTP_404_NOT_FOUND, {})
                return Response(status=status.HTTP_404_NOT_FOUND, data=response)
        except Exception as e:
            print('error:', e)
            response = make_response(status.HTTP_400_BAD_REQUEST, str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST, data=response)


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
