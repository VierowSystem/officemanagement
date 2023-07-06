from django.urls import path

from OfficeApp import views, userview

urlpatterns = [

    path('',views.main_home,name='homepage'),
    path('admindash/',views.admin_home,name='admindash'),
    path('login/',views.login_view,name='login'),

    # *********************** STOCK ************************************************

    path('Add_Stock/', views.stock_add, name='Add_Stock'),
    path('View_Stock/', views.stock_view, name='View_Stock'),
    path('update_stock/<int:id>/', views.update_stock, name='update_stock'),
    path('stock_delete/<int:id>/', views.stock_delete, name='stock_delete'),
    path('pdfstock', views.pdf_stock, name='pdfstock'),

    # *********************** ACCOUNT ************************************************

    path('Add_Account/', views.Account_add, name='Add_Account'),
    path('View_Account/', views.account_view, name='View_Account'),
    path('update_account/<int:id>/', views.update_account, name='update_account'),
    path('account_delete/<int:id>/', views.account_delete, name='account_delete'),
    path('pdfaccount', views.pdf_account, name='pdfaccount'),

    # *********************** SALES ************************************************

    path('Sales_add/', views.Sales_add, name='Add_Sale'),
    path('sale_view/', views.sale_view, name='View_Sale'),
    path('update_sales/<int:id>/', views.update_sales, name='update_sales'),
    path('sales_delete/<int:id>/', views.sales_delete, name='sales_delete'),
    path('create-pdf', views.pdf_sale, name='create-pdf'),

    # ****************************  EXPENSE ***********************************

    path('Expense_add/', views.Expense_add, name='Add_Expense'),
    path('expense_view/', views.expense_view, name='View_Expense'),
    path('update_expense/<int:id>/', views.update_expense, name='update_expense'),
    path('expense_delete/<int:id>/', views.expense_delete, name='expense_delete'),
    path('pdfexpense', views.pdf_expense, name='pdfexpense'),

    # **************************** EMPLOYEE ***********************************

    path('emp_register/', views.emp_register, name='empreg'),
    path('view_emp/', views.employee, name='view_emp'),
    path('user_delete/<int:id>/', views.emp_delete, name='user_delete'),
    path('emphome/', userview.user_home, name='emphome'),

    # **************************** EMP_EXPENSE ***********************************

    # path('empexpense_add/', userview.empexpense_add, name='empAdd_Expense'),
    path('empexpense_view/', userview.empexpense_view, name='empView_Expense'),
    path('empexpense_delete/<int:id>/', userview.empexpense_delete, name='empexpense_delete'),
    path('profile_view/', userview.profile_view, name='emp_pro'),



]