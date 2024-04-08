from django.shortcuts import render, redirect
from django.views import View 
from django.contrib import messages
from django.views import View
from django.db.models import Q

from django.core.paginator import Paginator

from django.shortcuts import render
from django.utils.translation import gettext as _

from core.models import Settings
from .models import ContactUs

from dashboard.forms import *
from dashboard.models import *
from blogs.models import Blog
from core.models import Settings
from vacancies.models import Job
from news.models import NewsArticle
from documents.models import Document


from django.core.paginator import Paginator

def paginate(object, number, request):
    
    p = Paginator(object, number)
    page = request.GET.get('page')
    obj_list = p.get_page(page)

    return obj_list


def index(request):
    recent_blogs = Blog.objects.order_by('-publish_date')[:4]
    recent_news = NewsArticle.objects.order_by('-created_at')[:4]
    map = Settings.objects.first().map_link if Settings.objects.first() else ''
    recent_documents = Document.objects.order_by('-upload_date')[:9]
    gallery_images = GalleryImage.objects.all()[:7]
    faqs = FAQ.objects.all()
    about_us = DirectorateMessage.objects.first()
    featured_works = FeaturedWork.objects.all()
    
    paragraphs = about_us.content[:800] + "..." if about_us else about_us
    paragraphs = paragraphs.split('\n') if paragraphs else paragraphs
    context = {
        'index':True,
        'recent_blogs': recent_blogs,
        'recent_news': recent_news,
        'recent_documents': recent_documents,
        'gallery_images': gallery_images,
        'faqs': faqs,
        'about_us': about_us,
        'paragraphs': paragraphs,  # Pass preprocessed paragraphs to template context
        'featured_works': featured_works,  # Add Featured Works data to context
        'map':map
        
    }
    return render(request, 'front/index.html', context)


def search(request): 
    if "searched_item" in request.GET:
        searched_term = request.GET["searched_item"]

        news = NewsArticle.objects.filter(Q(title__icontains=searched_term) | Q(news_category__name__icontains=searched_term) | Q(author__icontains=searched_term))
        blogs = Blog.objects.filter(Q(title__icontains=searched_term) | Q(blog_category__name__icontains=searched_term) | Q(author__icontains=searched_term))
        jobs = Job.objects.filter(Q(job_title__icontains=searched_term) | Q(job_type__icontains=searched_term) | Q(Status__icontains=searched_term), Status='Active')
        gallery = GalleryImage.objects.filter(Q(title__icontains=searched_term) | Q(gallery_category__name__icontains=searched_term))
        documents = Document.objects.filter(Q(title__icontains=searched_term) | Q(category__icontains=searched_term))
        events = Event.objects.filter(Q(title__icontains=searched_term) | Q(location__icontains=searched_term))
        
        if news.count() == 0 and blogs.count() == 0 and jobs.count() == 0 and gallery.count() == 0 and documents.count() == 0 and events.count() == 0:
            data =  {'no_result':True}
        else:
            data =  { 
                "news_articles": news,
                "blogs": blogs, 
                "images": gallery, 
                "jobs": jobs, 
                "documents": documents, 
                "events": events, 
                "term": searched_term,
            }
        
    else:
        data =  {'no_result':True}

    return render (request, 'front/search_results.html',data)
        

class GalleryImagePage(View): 
    def get(self, request):
        images= GalleryImage.objects.all()
        
        images_list = paginate( images, 12, request)

        context = {
            'images':images_list,
            'categories':[cat.name for cat in GalleryCategory.objects.all()],
        }

        return render(request, 'front/gallery.html', context)
    
    
class GalleryVideoPage(View):
    def get(self, *args, **kwargs):
        gallery_videos = GalleryVideo.objects.all()
        
        gallery_videos_list = paginate( gallery_videos, 5, self.request)

        categories = [cat.name for cat in GalleryCategory.objects.all()]
        return render(self.request, 'front/videos.html', {'gallery_videos':gallery_videos_list, 'categories':categories})

    
class EventListPage(View):
    def get(self,*args, **kwargs):
        events = Event.objects.all()
        
        events_list = paginate( events, 6, self.request)

        return render(self.request, 'front/event.html', {'events': events_list})


class Contact(View):
    def get (self, *args, **kwargs):
        map = Settings.objects.first().map_link if Settings.objects.first() else ''
        return render( self.request, 'front/contact.html', {'map':map})
    
    def post(self, *args, **kwargs):
        data = self.request.POST
        contact = ContactUs.objects.create(full_name = data['name'], email = data['email'], phone = data['phone'], subject = data['subject'], message = data['message'])
        contact.save()
        msg = f"A visitor called {data['name']} with a phone number of {data['phone']} has sent a message with a subject of {data['subject']}. \n {data['message']}"
        messages.success(self.request,"Successfully sent your feed back to our staff. We'll get back to you soon.")
        email = Settings.objects.first().email_for_contact_us if Settings.objects.first() else 'mukeraacc@gmail.com'
        e = EmailMultiAlternatives(f"Visitor message : {data['subject']}",msg,from_email="Kanenus",to=[str(email)]).send()
        # e = send_mail(f"Visitor message : {data['subject']}", msg, from_email="Kanenus", recipient_list=['antenyismu@gmail.com'], fail_silently=False)
        print(e)
        return redirect(self.request.path)         


class BidPage(View):
    def get(self, request):
        bids = Bid.objects.all()
        bids_list = paginate( bids, 5, self.request)
        return render(request, "front/bid.html", {'bids':bids_list})