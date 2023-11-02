from django.shortcuts import render
from .models import Cafe, Transaction, TransactionCancellation

def cafe_list(request):
    cafes = Cafe.objects.all()
    return render(request, 'cafe_list.html', {'cafes': cafes})

def transaction_list(request, cafe_id):
    cafe = Cafe.objects.get(id=cafe_id)
    transactions = Transaction.objects.filter(cafe=cafe)
    return render(request, 'transaction_list.html', {'cafe': cafe, 'transactions': transactions})

def cancel_transaction(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    if request.method == 'POST':
        reason = request.POST['reason']
        cancellation = TransactionCancellation.objects.create(transaction=transaction, reason=reason)
        transaction.delete()
        return render(request, 'cancellation_success.html', {'cancellation': cancellation})
    return render(request, 'cancel_transaction.html', {'transaction_id': transaction_id})
