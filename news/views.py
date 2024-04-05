
from django.shortcuts import render,  redirect
from.models import NewsArticle
from django.core.paginator import Paginator

def news_list_visitor(request):
    news_articles = NewsArticle.objects.all()
    
    p = Paginator(news_articles, 12)
    page = request.GET.get('page')
    news_article_list = p.get_page(page)

    return render(request, 'front/news.html', {'news_articles': news_article_list})

def news_detail(request, news_id):
    try:
        news_item = NewsArticle.objects.get(id=news_id)
    except Exception as e:
        # Handle the case where the news with the provided ID does not exist
        return redirect("news_list_visitor")

    

    return render(request, 'front/news_detail.html', {
        'news_item': news_item, 
        'lastnews':NewsArticle.objects.exclude(id = news_item.id)
        
    })
