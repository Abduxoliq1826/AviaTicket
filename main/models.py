from django.db import models

class Country(models.Model):
     name = models.CharField(max_length=255)

class City(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

class Ticket(models.Model):
    company = models.CharField(max_length=255)
    take_of_date = models.DateTimeField()
    boarding_date = models.DateTimeField()
    from_where = models.ForeignKey(City,max_length=255)
    where = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_baggage = models.ForeignKey(Bagggage, on_delete=models.CASCADE)