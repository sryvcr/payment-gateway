import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from payment_gateway.payments.business_logic.users import (
    get_user_by_id,
    get_credit_cards_by_user_id,
    create_user,
    link_credit_card,
    create_payment_token,
    update_user,
    delete_user
)
from payment_gateway.payments.serializers.user import (
    UserSerializer,
    UserCreateSerializer,
    LinkCreditCardSerializer,
    PaymentTokenSerializer
)
from payment_gateway.payments.serializers.credit_card import (
    CreditCardSerializer,
)
from payment_gateway.payments.utils.make_response import make_response


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


class CreditCardsGetByUserId(APIView):

    def get(self, request, uid: str):
        try:
            try:
                credit_cards = get_credit_cards_by_user_id(uid)
                serializer = CreditCardSerializer(credit_cards, many=True)
                response = make_response(status.HTTP_200_OK, serializer.data)
                print(response)
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


class LinkCreditCardView(APIView):

    def post(self, request):
        try:
            body = json.loads(request.body)
            user_link_credit_card = link_credit_card(
                credit_card_id=body['credit_card_id'],
                user_id=body['user_id']
            )
            serializer = LinkCreditCardSerializer(user_link_credit_card)
            response = make_response(status.HTTP_201_CREATED, serializer.data)
            return Response(status=status.HTTP_201_CREATED, data=response)
        except Exception as e:
            print('error:', e)
            response = make_response(status.HTTP_400_BAD_REQUEST, str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST, data=response)


class PaymentTokenCreateView(APIView):

    def post(self, request):
        try:
            body = json.loads(request.body)
            payment_token = create_payment_token(
                user_credit_card_id=body['user_credit_card_id'],
            )
            serializer = PaymentTokenSerializer(payment_token)
            response = make_response(status.HTTP_201_CREATED, serializer.data)
            return Response(status=status.HTTP_201_CREATED, data=response)
        except Exception as e:
            print('error:', e)
            response = make_response(status.HTTP_400_BAD_REQUEST, str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST, data=response)


class UserUpdateOneView(APIView):

    def patch(self, request, uid: str):
        try:
            try:
                user = get_user_by_id(uid)
            except:
                response = make_response(status.HTTP_404_NOT_FOUND, {})
                return Response(status=status.HTTP_404_NOT_FOUND, data=response)
            body = json.loads(request.body)
            user = update_user(uid, body)
            serializer = UserSerializer(user)
            response = make_response(status.HTTP_201_CREATED, serializer.data)
            return Response(status=status.HTTP_201_CREATED, data=response)
        except Exception as e:
            print('error:', e)
            response = make_response(status.HTTP_400_BAD_REQUEST, str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST, data=response)


class UserDeleteOneView(APIView):

    def delete(self, request, uid: str):
        try:
            try:
                user = get_user_by_id(uid)
            except:
                response = make_response(status.HTTP_404_NOT_FOUND, {})
                return Response(status=status.HTTP_404_NOT_FOUND, data=response)
            delete_user(user)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            print('error:', e)
            response = make_response(status.HTTP_400_BAD_REQUEST, str(e))
            return Response(status=status.HTTP_400_BAD_REQUEST, data=response)
