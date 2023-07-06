from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from OfficeApp.models import Expense
from django.shortcuts import render, redirect
from django.contrib import messages


def user_home(request):
    return render(request, 'emphome.html')


def profile_view(request):
    profile = [request.user.user]  # Wrap the user object in a list
    return render(request, 'emptemp/emp_pro.html', {'profile': profile})


# def empexpense_add(request):
#     if request.method == 'POST':
#         form = EmployeForm(request.POST)
#         if form.is_valid():
#             expense = form.save(commit=False)
#
#             if request.user.is_authenticated:
#                 expense.employee_name = request.user
#             else:
#                 # Handle the case where the user is not authenticated
#                 # For example, you can set a default user or do some other action
#                 expense.employee_name = None
#
#             expense.save()
#             messages.info(request, "Expense Added Successfully")
#             return redirect('empView_Expense')
#     else:
#         form = EmployeForm()
#
#     return render(request, 'emptemp/empAdd_Expense.html', {'form': form})


def empexpense_view(request):
    exp = Expense.objects.all()
    return render(request, 'emptemp/empView_Expense.html', {'exp': exp})


def empexpense_delete(request, id):
    n = Empexpense.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, " Deleted Successfully")
        return redirect('empView_Expense')
    else:
        return redirect('empView_Expense')


