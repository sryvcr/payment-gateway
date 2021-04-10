from django.urls import path
from .views import (
    CreditCardCreateOneView,
    CreditCardDeleteOneView
)


urlpatterns = [
    path('create-one', view=CreditCardCreateOneView.as_view(), name='credit_card_create_one'),
    path('delete-one/<str:uid>', view=CreditCardDeleteOneView.as_view(), name='credit_card_delete_one')
]
