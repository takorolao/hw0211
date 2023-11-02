from django.urls import path
from .views import cafe_list, transaction_list, cancel_transaction

urlpatterns = [
    path('', cafe_list, name='cafe_list'),
    path('cafe/<int:cafe_id>/', transaction_list, name='transaction_list'),
    path('transaction/<int:transaction_id>/cancel/', cancel_transaction, name='cancel_transaction'),
]
