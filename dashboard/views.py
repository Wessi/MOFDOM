from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from django.shortcuts import render,redirect
from .models import *
from about_us.models import AboutUs
from news.models import News,NewsArticle
from blogs.models import Blog
from documents.models import Document
from .forms import EventForm
from django.shortcuts import get_object_or_404

def admin_dashboard(request):
    return render(request, 'admin_home.html')

#new yismu template
def index(request):
    recent_blogs = Blog.objects.order_by('-publish_date')[:4]
    recent_news = NewsArticle.objects.order_by('-created_at')[:4]
    categories = Document.CATEGORY_CHOICES
    documents_by_category = {}
    for category, _ in categories:
        documents_by_category[category] = Document.objects.filter(category=category)

    gallery_categories = GalleryImage.CATEGORY_CHOICES
    gallery_images_by_category = {}
    for category, _ in gallery_categories:
        images = GalleryImage.objects.filter(category=category)
        image_data = [{'title': img.title, 'image_url': img.image.url} for img in images]
        gallery_images_by_category[category] = image_data

    # Fetch FAQs data
    faqs = FAQ.objects.all()

    # Fetch About Us data
    about_us = About_us_index.objects.first()
    if about_us:
        # Split content into paragraphs
        paragraphs = about_us.content.split('\n')

        context = {
            'recent_blogs': recent_blogs,
            'recent_news': recent_news,
            'categories': categories,
            'documents_by_category': documents_by_category,
            'gallery_images_by_category': gallery_images_by_category,
            'faqs': faqs,
            'about_us': about_us,
            'paragraphs': paragraphs,  # Pass preprocessed paragraphs to template context
        }
    else:
        context = {
            'recent_blogs': recent_blogs,
            'recent_news': recent_news,
            'categories': categories,
            'documents_by_category': documents_by_category,
            'gallery_images_by_category': gallery_images_by_category,
            'faqs': faqs,
        }

    return render(request, 'front/index.html', context)

def gallery_list_view(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallaries_list_admin.html', {'images': images})    

#new yismu template
def gallery_view(request):
    gallery_categories = GalleryImage.CATEGORY_CHOICES
    gallery_images_by_category = {}
    for category, _ in gallery_categories:
        images = GalleryImage.objects.filter(category=category)
        image_data = [{'title': img.title, 'image_url': img.image.url} for img in images]
        gallery_images_by_category[category] = image_data
    
    context = {
        'gallery_images_by_category': gallery_images_by_category,
    }
    return render(request, 'front/gallery.html', context)
    
def delete_gallery_image(request, image_id):
    image = get_object_or_404(GalleryImage, id=image_id)
    
    if request.method == 'POST':
        image.delete()
        return redirect('gallery_list_view')
    context = {'image': image}
    return render(request, 'delete_gallery_image.html', context)

    
    
def custom_admin(request):
    return render(request, 'back/master.html', {'suppliers': suppliers})
# views.py
@csrf_exempt
def add_faq_api(request):
    if request.method == 'POST':
        question = request.POST.get('question')
        answer = request.POST.get('answer')

        if question and answer:
            new_faq = FAQ(question=question, answer=answer)
            new_faq.save()

            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Missing required data'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
def faqs_api(request):
    faqs = FAQ.objects.all()
    faqs_list = [{'question': faq.question, 'answer': faq.answer} for faq in faqs]
    return JsonResponse({'faqs': faqs_list})
def add_footer_api(request):
    if request.method == 'POST':
        form = FooterForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid form data'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

def footer_api(request):
    footer_instance = Footer.objects.first()
    if footer_instance:
        data = {
            'about_us_content': footer_instance.about_us_content,
            'contact_info': footer_instance.contact_info,
            'projects_links': footer_instance.projects_links,
            'quick_links': footer_instance.quick_links,
            'newsletter_content': footer_instance.newsletter_content,
            'copyright_text': footer_instance.copyright_text,
        }
        return JsonResponse(data)
    else:
        return JsonResponse({'status': 'error', 'message': 'Footer content not found'})

def add_FAQs(request):
    return render(request, 'add_FAQs.html')
def add_gallarie_image(request):
    return render(request, 'gallarie_image_add.html')
def edit_footers(request):
    return render(request, 'footers.html')
def add_sliders(request):
    return render(request, 'sliders.html')

def privacy_index(request):
    return render(request, 'privacy_index.html')
    
def add_event_back(request):
    return render(request, 'add_event.html')
    
def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def Projects(request):
    return render(request, 'projects.html')

def gallarie_all(request):
    gallery_images = GalleryImage.objects.all()
    return render(request, 'gallaries_all.html', {
        'gallery_images': gallery_images,

    })

def add_gallarie_image_back(request):
    if request.method == 'POST':
        form = GalleryImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery_list_view')  # Redirect to the gallery image list view
    else:
        form = GalleryImageForm()

    return render(request, 'back_add_gallary.html', {'form': form})


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Redirect to the event list page after adding the event
    else:
        form = EventForm()

    return render(request, 'add_event.html', {'form': form})
    
#from yismu    
def events_list_new(request):
    events = Event.objects.all()
    return render(request, 'front/event.html', {'events': events})

def delete_faq(request, faq_id):
    faq = get_object_or_404(FAQ, id=faq_id)
    
    if request.method == 'POST':
        faq.delete()
        return redirect('faq_list')
    
    context = {'faq': faq}
    return render(request, 'delete_faqs.html', context)    
    
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events_list.html', {'events': events})  

def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)  # Retrieve the Event object

    if request.method == 'POST':
        event.delete()  # Delete the Event object
        return redirect('event_list')  # Redirect to the event list view

    context = {
        'event': event,
    }
    return render(request, 'delete_event.html', context)  # Render the delete_event.html template

def faq_list(request):
    faqs = FAQ.objects.all()
    return render(request, 'faqs_list.html', {'faqs': faqs})
