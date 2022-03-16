from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=50)

    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True

        return False
