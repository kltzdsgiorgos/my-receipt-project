from django.db import models

TAX = 0.24

class Receipt(models.Model):

    fill_date = models.DateTimeField('date filled')
    fuel_type = models.CharField(max_length=10)
    location = models.CharField(max_length=20)
    gas_station = models.CharField(max_length=10)
    price_per_liter = models.FloatField()
    liters = models.FloatField()
    gas_total_price = models.FloatField()

    def __str__(self):
        return str(self.fill_date) + self.fuel_type

    def calculate_tax(self):

        tax_price = self.gas_total_price * TAX
        
        return tax_price

    def calculate_total_paid(self):

        total_paid = self.tax_price + self.gas_total_price

        return total_paid