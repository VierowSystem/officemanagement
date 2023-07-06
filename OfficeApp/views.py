from io import BytesIO

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.forms import forms
from django.http import HttpResponse

from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse
import PyPDF2
from bs4 import BeautifulSoup


from OfficeApp.form import Stockform, LoginRegister, Userform, Accountform, Salesform, Expenseform
from OfficeApp.models import Stock, Account, Sales, User, Expense
from xhtml2pdf import pisa


def main_home(request):
    return render(request,'homepage.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass')
        user = authenticate(request, username=username, password=password)
        # print('hhjjkklloo')
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admindash')
            if user.is_user:
                return redirect('emphome')
        else:
            messages.info(request, "Invalid Credentials")
    return render(request, 'login.html')



def admin_home(request):
        return render(request,'admindash.html')

# ************     STOCKS       ******************            *******************            *****************

def stock_add(request):
    form = Stockform()
    if request.method == 'POST':
        print('ssssss')
        form = Stockform(request.POST)
        print('ttttttt')
        if form.is_valid():
            print('ooooo')
            form.save()
            messages.info(request, "Stock Added Successfully")
            return redirect('View_Stock')
    return render(request, 'admintemp/Add_Stock.html', {'form': form})


def stock_view(request):
    stock = Stock.objects.all()
    return render(request, 'admintemp/View_Stock.html', {'stock': stock})


def update_stock(request, id):
    n = Stock.objects.get(id=id)
    if request.method == 'POST':
        form = Stockform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            messages.info(request, "Stock Updated Successfully")
            return redirect('View_Stock')
    else:
        form = Stockform(request.POST or None, instance=n)
    return render(request, 'admintemp/update_stock.html', {'form': form})


def stock_delete(request, id):
    n = Stock.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, "Stock Deleted Successfully")
        return redirect('View_Stock')
    else:
        return redirect('View_Stock')

def pdf_stock(request):
    stock = Stock.objects.all()
    if request.method == 'GET':

        template_path = 'admintemp/pdfstock.html'

        context = {'stock': stock}

        response = HttpResponse(content_type='application/pdf')

        response['Content-Disposition'] = 'filename="products_report.pdf"'

        template = get_template(template_path)

        html = template.render(context)

    # create a pdf
        pisa_status = pisa.CreatePDF(
         html, dest=response)
    # if error then show some funy view
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response

# ************            ******************            *******************            *****************

# def emp_register(request):
#     if request.method == 'GET':
#         print("aaaaaa")
#         login_form = LoginRegister(request.GET ,prefix='login_form')
#         emp_form = Userform(request.GET,prefix='emp_form')
#         print("bbbbb")
#         if login_form.is_valid() and emp_form.is_valid():
#             print('ccccc')
#             u = login_form.save()
#             u.is_user = True
#             u.save()
#             print('ddddddd')
#             emp_form = emp_form.save()
#             emp_form.user = u
#             emp_form.save()
#             messages.info(request, "User Registered Successfully")
#             return redirect('login')
#     else:
#         login_form = LoginRegister(prefix='form1')
#         emp_form = Userform(prefix='form2')
#     return render(request, 'empreg.html', {'login_form': login_form, 'emp_form': emp_form})


# ************   ACCOUNTS         ******************            *******************            *****************

def Account_add(request):
    form = Accountform()
    if request.method == 'POST':
        form = Accountform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Accounts Added Successfully")
            return redirect('View_Account')
        else:
            print(form.errors)
    return render(request, 'admintemp/Add_Account.html', {'form': form})



def account_view(request):
    account = Account.objects.all()
    return render(request, 'admintemp/View_Account.html', {'account': account})

def update_account(request, id):
    n = Account.objects.get(id=id)
    if request.method == 'POST':
        form = Accountform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            messages.info(request, "Accounts Updated Successfully")
            return redirect('View_Account')
    else:
        form = Accountform(request.POST or None, instance=n)
    return render(request, 'admintemp/update_account.html', {'form': form})



def account_delete(request, id):
    n = Account.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, "Accounts Deleted Successfully")
        return redirect('View_Account')
    else:
        return redirect('View_Account')

def pdf_account(request):
    account = Account.objects.all()
    if request.method == 'GET':

        template_path = 'admintemp/pdfaccount.html'

        context = {'account': account}

        response = HttpResponse(content_type='application/pdf')

        response['Content-Disposition'] = 'filename="products_report.pdf"'

        template = get_template(template_path)

        html = template.render(context)

        pisa_status = pisa.CreatePDF(
            html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response


# ************      SALES      ******************            *******************            *****************

def Sales_add(request):
    if request.method == 'POST':
        form = Salesform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Sales Added Successfully")
            return redirect('View_Sale')
    else:
        form = Salesform()
    return render(request, 'admintemp/Add_Sale.html', {'form': form})


def sale_view(request):
    sale = Sales.objects.all()
    return render(request, 'admintemp/View_Sale.html', {'sale': sale})


def update_sales(request, id):
    n = Sales.objects.get(id=id)
    if request.method == 'POST':
        form = Salesform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            messages.info(request, "Accounts Updated Successfully")
            return redirect('View_Sale')
    else:
        form = Salesform(request.POST or None, instance=n)
    return render(request, 'admintemp/update_sales.html', {'form': form})


def sales_delete(request, id):
    n = Sales.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, "Accounts Deleted Successfully")
        return redirect('View_Sale')
    else:
        return redirect('View_Sale')


def pdf_sale(request):
    sale = Sales.objects.all()
    if request.method == 'GET':

        template_path = 'admintemp/pdfsale.html'

        context = {'sale': sale}

        response = HttpResponse(content_type='application/pdf')

        response['Content-Disposition'] = 'filename="products_report.pdf"'

        template = get_template(template_path)

        html = template.render(context)

        pisa_status = pisa.CreatePDF(
            html, dest=response)
        if pisa_status.err:
            return HttpResponse('We had some errors <pre>' + html + '</pre>')
        return response

# ************     EXPENSES       ******************            *******************            *****************


def Expense_add(request):
    form = Expenseform()
    if request.method == 'POST':
        form = Expenseform(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Expense Added Successfully")
            return redirect('View_Expense')
        else:
            print(form.errors)
    return render(request, 'admintemp/Add_Expense.html', {'form': form})


def expense_view(request):
    exp = Expense.objects.all()
    return render(request, 'admintemp/View_Expense.html', {'exp': exp})


def update_expense(request, id):
    n = Expense.objects.get(id=id)
    if request.method == 'POST':
        form = Expenseform(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            messages.info(request, "Expense Updated Successfully")
            return redirect('View_Expense')
    else:
        form = Expenseform(request.POST or None, instance=n)
    return render(request, 'admintemp/update_expense.html', {'form': form})


def expense_delete(request, id):
    n = Expense.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, "Expense Deleted Successfully")
        return redirect('View_Expense')
    else:
        return redirect('View_Expense')


def pdf_expense(request):
    exp = Expense.objects.all()

    if request.method == 'GET':
        template_path = 'admintemp/pdfexpense.html'
        context = {'exp': exp}

        template = get_template(template_path)
        html = template.render(context)
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table')
        total_values = [float(cell['data-total']) for cell in table.find_all('td', {'data-total': True})]
        total_sum = sum(total_values)

        total_sum_tag = soup.new_tag('span')
        total_sum_tag.string = f'TOTAL : {total_sum}'
        table.insert_after(total_sum_tag)


        modified_html = str(soup)
        buffer = BytesIO()
        pisa.CreatePDF(BytesIO(modified_html.encode('utf-8')), dest=buffer)
        pdf_content = buffer.getvalue()
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'filename="pdfexpense.pdf"'
        response.write(pdf_content)

        return response
# ************     USER       ******************            *******************            *****************


def emp_register(request):
    if request.method == 'POST':
        login_form = LoginRegister(request.POST)
        user_form = Userform(request.POST)

        if login_form.is_valid() and user_form.is_valid():
            user = login_form.save(commit=False)
            user.is_user = True
            user.save()

            user_profile = user_form.save(commit=False)
            user_profile.user = user
            user_profile.save()

            # Clear form errors
            login_form.errors.clear()
            user_form.errors.clear()
    else:
        login_form = LoginRegister()
        user_form = Userform()

    return render(request, 'empreg.html', {'login_form': login_form, 'user_form': user_form})


@login_required
def employee(request):
    user = User.objects.all()
    return render(request, 'admintemp/view_emp.html', {'user': user})

def emp_delete(request, id):
    n = User.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, "User Deleted Successfully")
        return redirect('view_emp')
    else:
        return redirect('view_emp')



