from django.urls import path
from .views import (
    CreditCardCreateOneView
)


urlpatterns = [
    path('create-one', view=CreditCardCreateOneView.as_view(), name='credit_card_create_one')
]
