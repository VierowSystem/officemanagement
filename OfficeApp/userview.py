from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from OfficeApp.form import UserForm, Itemform
from OfficeApp.models import Expense, User, Item
from django.shortcuts import render, redirect
from django.contrib import messages

@login_required
def user_home(request):
    return render(request, 'emphome.html')

@login_required
def profile_view(request):
    profile = [request.user.user]  # Wrap the user object in a list
    return render(request, 'emptemp/emp_pro.html', {'profile': profile})

@login_required
def profile_update(request,user_id):
    n = User.objects.get(user_id=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST or None, instance=n)
        if form.is_valid():
            form.save()
            messages.info(request, "Profile Updated Successfully")
            return redirect('emp_pro')
    else:
        form = UserForm(request.POST or None, instance=n)
    return render(request, 'emptemp/profile_update.html', {'form': form})


@login_required
def empexpense_view(request):
    exp = Expense.objects.all()
    return render(request, 'emptemp/empView_Expense.html', {'exp': exp})


@login_required
def empexpense_delete(request, id):
    n = Expense.objects.get(id=id)
    if request.method == 'POST':
        n.delete()
        messages.info(request, " Deleted Successfully")
        return redirect('empView_Expense')
    else:
        return redirect('empView_Expense')



@login_required
def item_add(request):
    form = Itemform()
    u = request.user
    if request.method == 'POST':
        form = Itemform(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = u
            obj.save()
            messages.info(request, "Item Added Successfully")
            return redirect('emphome')
        else:
            print(form.errors)
    return render(request, 'emptemp/itemadd.html', {'form': form})

def empitem_view(request):
    print(request.user)  # Debug statement to check the value of request.user

    # Filter items based on the current user
    items = Item.objects.filter(user=request.user)

    return render(request, 'emptemp/empitemview.html', {'items': items})



