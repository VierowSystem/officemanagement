from django.contrib.auth.models import AbstractUser
from django.db import models


class Login(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)
    contact_no = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class User(models.Model):
    user = models.OneToOneField(Login, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Account(models.Model):
    dateof_purchase = models.DateField()
    vendor = models.CharField(max_length=100)
    particular = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    gst_num = models.IntegerField()
    sale_amt = models.IntegerField()
    qty = models.IntegerField()
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
    invoice_num = models.IntegerField(unique=True, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.invoice_num:
            # Generate a new invoice number logic
            latest_invoice = Account.objects.order_by('-invoice_num').first()
            if latest_invoice:
                self.invoice_num = latest_invoice.invoice_num + 1
            else:
                self.invoice_num = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.vendor



class Stock(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=100)
    invoice_no = models.IntegerField(unique=True, null=True, blank=True)
    particular = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    unit_price = models.IntegerField()
    qty = models.IntegerField()
    units = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    usage_qty = models.IntegerField()
    balance = models.IntegerField()
    invoice = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='stock_items', null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.invoice_no:
            # Generate a new invoice number logic
            latest_invoice = Stock.objects.order_by('-invoice_no').first()
            if latest_invoice:
                self.invoice_no = latest_invoice.invoice_no + 1
            else:
                self.invoice_no = 1
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name




class Sales(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=200)
    particular = models.CharField(max_length=100)
    quantity_sold = models.IntegerField()
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
    invoice_no = models.IntegerField()

class Expense(models.Model):
    date = models.DateField()
    site = models.CharField(max_length=200)
    emp_name = models.CharField(max_length=200)
    travel_exp = models.IntegerField()
    food = models.IntegerField()
    tea = models.IntegerField()
    other = models.IntegerField()
    total = models.IntegerField()


class Item(models.Model):
    user = models.ForeignKey(Login, on_delete=models.CASCADE)
    date = models.DateField()
    item_name = models.CharField(max_length=200)
    number = models.IntegerField()
    description = models.CharField(max_length=100)
    brand = models.CharField(max_length=200)
    is_approved = models.BooleanField(default=False)
    is_rejected = models.BooleanField(default=False)


