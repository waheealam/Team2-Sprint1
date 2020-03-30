from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

now = timezone.now()
def home(request):
   return render(request, 'retirecenterapp/home.html',
                 {'retirecenterapp': home})

@login_required
def order_list(request):
   orders = Order.objects.filter(created_date__lte=timezone.now())
   return render(request, 'retirecenterapp/order_list.html', {'orders': orders})

@login_required
def order_new(request):
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.created_date = timezone.now()
            order.save()
            orders = Order.objects.filter(created_date__lte=timezone.now())
            return render(request, 'retirecenterapp/order_list.html', {'orders': orders})
    else:
       form = OrderForm()
    return render(request, 'retirecenterapp/order_new.html', {'form': form})

@login_required
def order_edit(request, pk):
    order = get_object_or_404(Order, pk=pk)
    if request.method == "POST":
       # update
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.updated_date = timezone.now()
            order.save()
            order = Order.objects.filter(created_date__lte=timezone.now())
            return render(request, 'retirecenterapp/order_list.html', {'orders': order})
    else:
        # edit
       form = OrderForm(instance= order)
    return render(request, 'retirecenterapp/order_edit.html', {'form': form})

@login_required
def order_delete(request, pk):
    order = get_object_or_404(Order, pk=pk)
    order.delete()
    return redirect('retirecenterapp/order_list')

@login_required
def profile_display(request):
    profile = Profile.objects.filter(user__username=request.user)
    return render(request, 'retirecenterapp/profile_display.html', {'profile': profile})


@login_required
def profile_edit(request):
    profile = Profile.objects.filter(user__username=request.user)
    if request.method == "POST":
       # update
        form = ProfileFrom(request.POST, user__username=request.user)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.updated_date = timezone.now()
            profile.save()
            return render(request, 'retirecenterapp/profile_display.html', {'profile': profile})
    else:
        # edit
       form = ProfileForm(user__username=request.user)
    return render(request, 'retirecenterapp/order_edit.html', {'form': form})
