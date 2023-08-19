from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from OfficeApp.models import Stock, Account, Expense, Sales, User, Item


def manager_home(request):
    return render(request,'managerhome.html')


@login_required
def mstock_view(request):
    stock = Stock.objects.all()
    return render(request, 'manager/mview_stock.html', {'stock': stock})


@login_required
def maccount_view(request):
    account = Account.objects.all()
    return render(request, 'manager/mview_accounts.html', {'account': account})


@login_required
def mexpense_view(request):
    exp = Expense.objects.all()
    return render(request, 'manager/mview_exp.html', {'exp': exp})


@login_required
def msale_view(request):
    sale = Sales.objects.all()
    return render(request, 'manager/mview_sale.html', {'sale': sale})

@login_required
def memployee(request):
    user = User.objects.all()
    return render(request, 'manager/mview_emp.html', {'user': user})


def item_view(request):
    items = Item.objects.all()
    return render(request, 'manager/item_view.html', {'items': items})


@login_required
def approve_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.is_approved = True
    item.is_rejected = False
    item.save()
    return redirect('item_view')

@login_required
def reject_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.is_approved = False
    item.is_rejected = True
    item.save()
    return redirect('item_view')

