from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Sales, Stock

@receiver(post_save, sender=Sales)
def update_stock_on_sale(sender, instance, **kwargs):
    stock_items = Stock.objects.filter(particular=instance.particular, invoice_no=instance.invoice_no)

    sold_quantity = instance.quantity_sold

    for stock_item in stock_items:
        available_quantity = stock_item.qty

        if sold_quantity > available_quantity:
            sold_quantity = available_quantity

        stock_item.qty -= sold_quantity
        stock_item.save()