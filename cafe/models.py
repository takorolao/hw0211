from django.db import models

class Cafe(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    cafe = models.ForeignKey(Cafe, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Transaction #{self.id} - {self.amount}'
    

class TransactionCancellation(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return f'Cancellation for Transaction #{self.transaction.id}'

