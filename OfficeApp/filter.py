from OfficeApp.models import Stock, Sales
from django import forms
from django_filters import CharFilter
import django_filters



class StockFilter(django_filters.FilterSet):
    # name = CharFilter(field_name='invoice_no', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
    #     'placeholder': 'invoice_no ', 'class': 'form-control'}))

    class Meta:
        model = Stock
        fields = ('invoice_no',)


class SalesFilter(django_filters.FilterSet):
    # name = CharFilter(field_name='invoice_no', label="", lookup_expr='icontains', widget=forms.TextInput(attrs={
    #     'placeholder': 'Search Name', 'class': 'form-control'}))

    class Meta:
        model = Sales
        fields = ('invoice_no',)