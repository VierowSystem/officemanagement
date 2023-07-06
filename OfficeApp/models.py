
# Create your models here.

from django.contrib.auth.models import AbstractUser
from django.db import models




# Create your models here.


class Login(AbstractUser):
    is_user = models.BooleanField(default=False)



class User(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Stock(models.Model):
    stock_name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    stock_no = models.IntegerField()
    model = models.CharField(max_length=100)

    def __str__(self):
        return self.stock_name


class Account(models.Model):
    dateof_purchase = models.DateField()
    vendor = models.CharField(max_length=100)
    invoice_num = models.IntegerField()
    gst_num = models.IntegerField()
    sale_amt = models.IntegerField()
    freight_charge = models.IntegerField()
    taxable_value = models.IntegerField()
    sgst = models.IntegerField()
    cgst = models.IntegerField()
    round_off = models.FloatField()
    igst = models.IntegerField()
    amount1 = models.IntegerField()
    site = models.CharField(max_length=100)
    dateof_payment = models.DateField()
    payment_mode = models.CharField(max_length=100)
    amount2 = models.IntegerField()
    balance = models.IntegerField()
    paid_by = models.CharField(max_length=100)

    def __str__(self):
        return self.vendor


class Sales(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=200)
    invoice_no = models.CharField(max_length=200)
    gst_no = models.IntegerField()
    total = models.IntegerField()
    discount_allowed = models.IntegerField()
    sub_total = models.IntegerField()
    sgst = models.IntegerField()
    cgst = models.IntegerField()
    grand_total = models.IntegerField()
    pay_date = models.DateField()
    amt_recieved = models.IntegerField()
    outstanding = models.IntegerField()
    mode_of_payment = models.CharField(max_length=100)
    payment_status = models.CharField(max_length=100)


class Expense(models.Model):
    date = models.DateField()
    site = models.CharField(max_length=200)
    emp_name = models.CharField(max_length=200)
    travel_exp = models.IntegerField()
    food = models.IntegerField()
    tea = models.IntegerField()
    other = models.IntegerField()
    total = models.IntegerField()


#
# class Empexpense(models.Model):
#     employee_name = models.CharField(max_length=100)
#     date = models.DateField()
#     site = models.CharField(max_length=200)
#     travel_exp = models.IntegerField()
#     food = models.IntegerField()
#     tea = models.IntegerField()
#     other = models.IntegerField()
