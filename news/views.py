
from django.shortcuts import render, get_object_or_404, redirect
from.models import NewsArticle
from .forms import NewsArticleForm


#for the yismu template
def news_list_visitor(request):
    news_articles = NewsArticle.objects.all()
    return render(request, 'front/news.html', {'news_articles': news_articles})

def delete_news_article(request, article_id):
    article = get_object_or_404(NewsArticle, id=article_id)
    
    if request.method == 'POST':
        article.delete()
        return redirect('news_list')
    return render(request, 'delete_news.html', {'article': article})    
    
def update_news(request, news_id):
    news_article = get_object_or_404(NewsArticle, id=news_id)

    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES, instance=news_article)
        if form.is_valid():
            form.save()
            return redirect('news_list')  # Assuming you have a URL pattern named 'news_list' for listing news
    else:
        form = NewsArticleForm(instance=news_article)

    return render(request, 'update_news.html', {'form': form, 'news_article': news_article})

def news_detail(request, news_id):
    try:
        news_item = NewsArticle.objects.get(id=news_id)
    except Exception as e:
        # Handle the case where the news with the provided ID does not exist
        return redirect("news_list_visitor")

    

    return render(request, 'front/news_detail.html', {
        'news_item': news_item, 
        
    })


def add_news_article(request):
    if request.method == 'POST':
        form = NewsArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('news_list')  # Redirect to the news list page after adding the news article
    else:
        form = NewsArticleForm()

    return render(request, 'add_news_article_back.html', {'form': form})

def news_list(request):
    news_articles = NewsArticle.objects.all()
    return render(request, 'view_news_back.html', {'news_articles': news_articles})
