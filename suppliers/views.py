from django.shortcuts import render, get_object_or_404, redirect
from.forms import SupplierForm
from .models import Supplier
from django.db.models import Q

def view_supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_list.html', {'suppliers': suppliers, 'result':True})
    # return render(request, 'table.html', {'suppliers': suppliers, 'result':True})


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

