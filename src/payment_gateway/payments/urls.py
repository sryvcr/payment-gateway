from django.urls import path
from .views.credit_cards import (
    CreditCardGetByPk,
    CreditCardCreateOneView,
    CreditCardDeleteOneView
)
from .views.users import (
    UserGetByPk,
    CreditCardsGetByUserId,
    UserCreateOneView,
    LinkCreditCardView,
    PaymentTokenCreateView,
    UserUpdateOneView,
    UserDeleteOneView,
)
from .views.payments import (
    PaymentGetByPkView,
    PaymentCreateOneView,
    RepaymentCreateOneView
)


urlpatterns = [
    path('credit-cards/get-one/<str:uid>', view=CreditCardGetByPk.as_view(), name='credit_card_get_one'),
    path('credit-cards/create-one', view=CreditCardCreateOneView.as_view(), name='credit_card_create_one'),
    path('credit-cards/delete-one/<str:uid>', view=CreditCardDeleteOneView.as_view(), name='credit_card_delete_one'),

    path('users/get-one/<str:uid>', view=UserGetByPk.as_view(), name='user_get_one'),
    path('users/get-credit-cards/<str:uid>', view=CreditCardsGetByUserId.as_view(), name='user_update_one'),
    path('users/create-one', view=UserCreateOneView.as_view(), name='user_create_one'),
    path('users/link-credit-card', view=LinkCreditCardView.as_view(), name='user_link_credit_card'),
    path('users/create-payment-token', view=PaymentTokenCreateView.as_view(), name='user_create_payment_token'),
    path('users/update-one/<str:uid>', view=UserUpdateOneView.as_view(), name='user_update_one'),
    path('users/delete-one/<str:uid>', view=UserDeleteOneView.as_view(), name='user_delete_one'),

    path('payments/get-one/<str:uid>', view=PaymentGetByPkView.as_view(), name='payment_get_one'),
    path('payments/create-one', view=PaymentCreateOneView.as_view(), name='payment_create_one'),
    path('repayments/create-one', view=RepaymentCreateOneView.as_view(), name='repayment_create_one'),
]
