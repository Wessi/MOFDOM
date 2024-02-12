from django.shortcuts import render, get_object_or_404, redirect
from.forms import SupplierForm
from .models import Supplier
def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/suppliers/supplier/view')
    else:
        form = SupplierForm()

    return render(request, 'add_supplier.html', {'form': form})
def delete_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)

    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_view')

    context = {
        'supplier': supplier,
    }
    return render(request, 'delete_supplier.html', context)
def update_supplier(request, supplier_id):
    supplier = get_object_or_404(Supplier, id=supplier_id)

    if request.method == 'POST':
        form = SupplierForm(request.POST, instance=supplier)
        if form.is_valid():
            form.save()
            return redirect('supplier_view')
    else:
        form = SupplierForm(instance=supplier)

    context = {
        'form': form,
        'supplier': supplier,
    }
    return render(request, 'update_supplier.html', context)
def view_supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, 'view_supplier.html', {'suppliers': suppliers})
def view_supplier_admin(request):
    suppliers_admin = Supplier.objects.all()
    return render(request, 'admin_home.html', {'suppliers_admin': suppliers_admin})