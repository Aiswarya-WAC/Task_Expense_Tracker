from django.db import models

class Transaction(models.Model):
    transaction_type = models.CharField(max_length=50)  #
    amount = models.IntegerField()
    category = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return f"{self.transaction_type}: {self.category} - {self.amount}"
