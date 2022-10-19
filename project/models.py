from django.db import models

# TODO: Check if the customer wants to login, if they do then move this model to different app along with a user manager
class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Address(models.Model):
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

class Birq(models.Model):
    type = models.CharField(max_length=100, choices=[('300', '300'), ('600', '600'), ('2400', '2400')])
    quantity = models.IntegerField(default=0)

class Project(models.Model):
    name = models.CharField(max_length=255)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    type = models.CharField(choices=[('wall','Wall'),('house','House')], max_length=100)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    birq = models.ManyToManyField(Birq)
