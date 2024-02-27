from django.shortcuts import render, get_object_or_404, redirect
from.forms import SupplierForm
from .models import Supplier
from django.db.models import Q
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
    return render(request, 'supplier_list.html', {'suppliers': suppliers, 'result':True})


def search_supplier(request):

    if "searched_term" in request.GET:
        searched_supplier= request.GET["searched_term"]

        suppliers = Supplier.objects.filter(Q(company_name__icontains=searched_supplier) | Q(tin__icontains=searched_supplier) | Q(sector__icontains=searched_supplier))
        
        context = {"suppliers": suppliers, 'result':True }
        
        if suppliers.count() == 0: 

            context = {'result':False}
    
    else:
        context =  {'result':False}
    return render(request, 'supplier_list.html', context)


def view_supplier_admin(request):
    suppliers = Supplier.objects.all()
    return render(request, 'view_supplier.html', {'suppliers': suppliers})