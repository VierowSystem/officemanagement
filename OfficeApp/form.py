import re
from datetime import datetime

from django import forms
from django.contrib.auth.forms import UserCreationForm


from OfficeApp.models import Login, User, Stock, Account, Sales, Expense, Item


def phone_number_validator(value):
    # Regular expression pattern for a basic phone number format
    pattern = r'^\d{10}$'
    return re.match(pattern, value) is not None


class LoginRegister(UserCreationForm):
    username = forms.CharField(label='User_Name')
    password1 = forms.CharField(label='PASSWORD', widget=forms.PasswordInput)
    password2 = forms.CharField(label='CONFIRM PASSWORD', widget=forms.PasswordInput)

    class Meta(UserCreationForm.Meta):
        model = Login
        fields = ('username', 'password1', 'password2')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name', 'contact_no')

    def clean_username(self):
        name = self.cleaned_data['name']
        if User.objects.filter(name=name).exists():
            raise forms.ValidationError('A user with that name already exists.')
        return name


class Stockform(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('date', 'name', 'invoice_no', 'particular', 'model', 'unit_price', 'qty', 'units', 'site', 'usage_qty','balance')


class Accountform(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('dateof_purchase', 'vendor','particular','model','gst_num', 'sale_amt','qty','freight_charge', 'taxable_value', 'sgst',
                  'cgst', 'round_off', 'igst', 'amount1', 'site', 'dateof_payment', 'payment_mode', 'amount2', 'balance', 'paid_by','invoice_num',)

        def clean_dateof_purchase(self):
            dateof_purchase = self.cleaned_data['dateof_purchase']
            # Add date validation logic here
            # You can use date parsing libraries like datetime or dateutil to parse and validate the date
            # For example, using datetime module:
            try:
                datetime.datetime.strptime(dateof_purchase, '%Y-%m-%d')
            except ValueError:
                raise forms.ValidationError('Enter a valid date.')

            return dateof_purchase


class Salesform(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ('date', 'name', 'particular','quantity_sold', 'invoice_no', 'gst_no', 'total', 'discount_allowed', 'sub_total', 'cgst', 'sgst','grand_total',
                   'pay_date', 'amt_recieved', 'outstanding', 'mode_of_payment', 'payment_status')


class Expenseform(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('date', 'site', 'emp_name', 'travel_exp', 'food', 'tea', 'other', 'total')

class Itemform(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('date', 'item_name', 'number', 'description', 'brand', 'is_approved', 'is_rejected')


class ManagerRegistrationForm(forms.Form):
    # Your form fields and validation methods here (same as in your original code)

    def save(self):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password1')

        # Create the manager using the custom Login model
        user = Login.objects.create_user(username=username, email=email, password=password)
        user.is_manager = True
        user.save()  # Save the user object with is_manager set to True

        return user

