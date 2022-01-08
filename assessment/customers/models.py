from django.db import models


class Customer(models.Model):
    client_id = models.IntegerField(unique=True)
    full_name = models.CharField(max_length=50)
    status = models.TextField()
    mobile_number = models.CharField(max_length=20)
    office_name = models.CharField(max_length=50)
