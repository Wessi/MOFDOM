from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
from django.shortcuts import render, redirect, get_object_or_404


def document_list(request):
    # Retrieve all documents
    documents = Document.objects.all()

    # Get unique categories from the documents
    categories = set(document.category for document in documents)

    # Create a dictionary to store categorized documents
    categorized_documents = {category: [] for category in categories}

    # Categorize the documents
    for document in documents:
        categorized_documents[document.category].append(document)
        

    context = {
        'categorized_documents': categorized_documents,
    }

    return render(request, 'doc.html', context)
def doc_view(request):
    return render(request, 'document.html')
    
    
def delete_document(request, document_id):
    # document = get_object_or_404(Document, id=document_id)
    document = Document.objects.get(id = document_id)
    
    if request.method == 'POST':
        document.delete()
        return redirect('document_view')  # Change 'document_list' to the URL name of your document list view

    context = {
        'document': document,
    }
    return render(request, 'delete_doc.html', {'document': document})



def doc_view_menu(request):
    # Fetch all documents grouped by category
    document_categories = {}
    for category, _ in Document.CATEGORY_CHOICES:
        documents = Document.objects.filter(category=category)
        document_categories[category] = documents

    return render(request, 'base.html', {'document_categories': document_categories})

def add_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print("Document saved successfully")
            return redirect('document_view')
        else:
            print("Form has errors:", form.errors)
    else:
        form = DocumentForm()
    return render(request, 'doecument_add.html', {'form': form})
def document_view(request):
    documents = Document.objects.all()
    return render(request, 'document_view.html', {'documents': documents})
    
#new view for yismu template
def list_docs_view(request):
    documents = Document.objects.all()
    categories = Document.CATEGORY_CHOICES
    documents_by_category = {}
    for category, _ in categories:
        documents_by_category[category] = Document.objects.filter(category=category)


    context = {
        'categories': categories,
        'documents_by_category': documents_by_category,
        'documents':documents,
    }
    return render(request, 'front/docs.html', context)


def update_document(request, document_id):
    document = get_object_or_404(Document, id=document_id)

    if request.method == 'POST':
        form = DocumentForm(request.POST, instance=document)
        if form.is_valid():
            form.save()
            return redirect('document_view')
    else:
        form = DocumentForm(instance=document)

    context = {
        'form': form,
        'document': document,
    }
    return render(request, 'update_document.html', context)
