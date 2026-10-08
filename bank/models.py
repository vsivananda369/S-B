from django.db import models


class Customer(models.Model):

    first_name = models.CharField(max_length=100)

    last_name = models.CharField(max_length=100)

    mobile = models.CharField(max_length=15)

    email = models.EmailField(unique=True)

    # Demo fields only.
    # Do not use real PAN/Aadhaar information.
    pan_number = models.CharField(max_length=10)

    aadhaar_number = models.CharField(max_length=12)

    account_number = models.CharField(
        max_length=20,
        unique=True
    )

    balance = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=10000
    )

    def __str__(self):
        return self.first_name + " " + self.last_name