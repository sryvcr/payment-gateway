from django.urls import path
from .views import (
    CreditCardGetByPk,
    CreditCardCreateOneView,
    CreditCardDeleteOneView
)
from .view.users import (
    UserCreateOneView
)


urlpatterns = [
    path('credit-cards/get-one/<str:uid>', view=CreditCardGetByPk.as_view(), name='credit_card_get_one'),
    path('credit-cards/create-one', view=CreditCardCreateOneView.as_view(), name='credit_card_create_one'),
    path('credit-cards/delete-one/<str:uid>', view=CreditCardDeleteOneView.as_view(), name='credit_card_delete_one'),

    path('users/create-one', view=UserCreateOneView.as_view(), name='credit_card_create_one')
]
