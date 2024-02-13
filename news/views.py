from .models import Newsletter
from django.shortcuts import render, get_object_or_404, redirect
from .models import News
from .models import Main
from django.core.files.storage import FileSystemStorage  # for upload image
import datetime  # for date and time
from .models import SubCat   # To count news
from .models import Comment
from.models import Cat,NewsArticle
from .forms import NewsArticleForm
from.models import Trending
import random
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


#for the yismu template
def news_list_visitor(request):
    news_articles = NewsArticle.objects.all()
    return render(request, 'front/news.html', {'news_articles': news_articles})
def delete_news_article(request, article_id):
    article = get_object_or_404(NewsArticle, id=article_id)
    
    if request.method == 'POST':
        article.delete()
        return redirect('news_article_list')
    return render(request, 'delete_news.html', {'article': article})    
    
def home(request):
    # Fetch the latest news for the home page
    latest_news_home = News.objects.filter(show=1).order_by('-date', '-time')[:]
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    popnews = News.objects.all().order_by('-show')
    popnews2 = News.objects.all().order_by('-show')[:3]
    all_news = News.objects.all().order_by('-pk')
    last_news = News.objects.all().order_by('-pk')[:3]
    news_articles = NewsArticle.objects.all().order_by('-pk')

    return render(request, 'front/home.html', {
        'latest_news_home': latest_news_home,
        'cat': cat,
        'subcat': subcat,
        'popnews': popnews,
        'popnews2': popnews2,
        'all_news': all_news,
        'last_news': last_news,
        'news_articles':news_articles
    })
def index_news(request):
    # Fetch the latest news for the index page
    last_news = News.objects.all().order_by('-pk')[:4]
    return render(request, 'index.html', {
        'last_news': last_news,
    })
def news_letter(request):
    if request.method == 'POST':
        txt = request.POST.get('txt')
        res = txt.find('@')
        if int(res) != -1:
            b = Newsletter(txt=txt, status=1)
            b.save()
        else:
            try:
                int(txt)
                b = Newsletter(txt=txt, status=2)
                b.save()

            except:
                return redirect('home')

    return redirect('home')
def news_emails(request):
    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    emails = Newsletter.objects.filter(status=1)
    return render(request, 'back/emails.html', {'emails': emails})
def news_phones(request):
    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')  # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    phones = Newsletter.objects.filter(status=2)

    return render(request, 'back/phones.html', {'phones': phones})
##--#--## Delete Newsletter (Emails and Phones) Function For Back (Admin Panel - Backend) Start ##--#--##
def news_txt_del(request, pk, num):
    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')  # when user is not logged in, it will take you the login page(mylogin)
    # Login check End

    b = Newsletter.objects.get(pk=pk)
    b.delete()

    if int(num) == 2:
        return redirect('news_phones')
    return redirect('news_emails')
##--#--## Delete Newsletter (Emails and Phones) Function For Back (Admin Panel - Backend) End ##--#--##
def news_detail(request, news_id):
    try:
        news_item = NewsArticle.objects.get(id=news_id)
    except Exception as e:
        # Handle the case where the news with the provided ID does not exist
        return redirect("news_list_visitor")

    news = News.objects.all().order_by('-pk')
    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]
    popnews = News.objects.all().order_by('-pk')[:3]
    popnews2 = News.objects.all().order_by('-pk')[:3]
    trending = Trending.objects.all().order_by('-pk')[:3]

    
    

    # link = f"/urls/{news_item.rand}" if news_item else ""
    link  = "/"

    return render(request, 'front/news_detail.html', {
        'news': news, 'cat': cat, 'subcat': subcat, 'lastnews': lastnews, 'news_item': news_item,
        'popnews': popnews, 'popnews2': popnews2, 'trending': trending, 
        'link': link
    })


def news_detail_short(request, pk):
    site = Main.objects.get(pk=2)
    news = News.objects.all().order_by(
        '-pk')

    cat = Cat.objects.all()
    subcat = SubCat.objects.all()
    lastnews = News.objects.all().order_by('-pk')[:3]

    shownews = News.objects.filter(rand=pk)
    popnews = News.objects.all().order_by('-show')

    popnews2 = News.objects.all().order_by('-show')[:3]

    trending = Trending.objects.all().order_by('-pk')[
               :3]

    tagname = News.objects.get(rand=pk).tag  ### For tags
    tag = tagname.split(',')  ## It will divide your tags by comma(,). Can also by space or dot or what i want
    try:
        mynews = News.objects.get(rand=pk)
        mynews.show = mynews.show + 1
        mynews.save()

    except:
        print("Can't Add Show")
    link = "/urls/" + str(News.objects.get(name=word).rand)  ## For QR Code

    return render(request, 'front/news_detail.html',
                  {'site': site, 'news': news, 'cat': cat, 'subcat': subcat, 'lastnews': lastnews, 'shownews': shownews,
                   'popnews': popnews, 'popnews2': popnews2, 'tag': tag, 'trending': trending, 'link': link})
def news_list(request):
    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        news = News.objects.filter(writer=request.user)
    elif perm == 1:
        newss = News.objects.all()
        paginator = Paginator(newss, 7)
        page = request.GET.get('page')

        try:
            news = paginator.page(page)

        except EmptyPage:
            news = paginator.page(paginator.num_page)

        except PageNotAnInteger:
            news = paginator.page(1)
            # -# Pagination End #-#

    return render(request, 'back/news_list.html', {'news': news})
def news_add(request):
    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day

    if len(str(day)) == 1:
        day = "0" + str(day)
    if len(str(month)) == 1:
        month = "0" + str(month)

    today = str(year) + "/" + str(month) + "/" + str(day)
    time = str(now.hour) + ":" + str(now.minute)
    date = str(year) + str(month) + str(day)
    randint = str(random.randint(1000, 9999))
    rand = date + randint
    rand = int(rand)

    while len(News.objects.filter(rand=rand)) != 0:
        randint = str(random.randint(1000, 9999))
        rand = date + randint
        rand = int(rand)
    cat = SubCat.objects.all()

    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')
        newscat = request.POST.get('newscat')
        newstxtshort = request.POST.get('newstxtshort')
        newstxt = request.POST.get('newstxt')
        newsid = request.POST.get('newscat')

        tag = request.POST.get('tag')

        if newstitle == "" or newstxtshort == "" or newstxt == "" or newscat == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error': error})

        try:
            # -#-# Upload File Start #-#-#
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
            if str(myfile.content_type).startswith("image"):

                if myfile.size < 5000000:  ## Check File Size ##

                    newsname = SubCat.objects.get(pk=newsid).name  # query

                    ocatid = SubCat.objects.get(pk=newsid).catid  # get the total news for count news.

                    b = News(name=newstitle, short_txt=newstxtshort, body_txt=newstxt, date=today, picname=filename,
                             picurl=url, writer=request.user, catname=newsname, catid=newsid, show=0, time=time,
                             ocatid=ocatid, tag=tag, rand=rand)  # these are the model fields
                    b.save()

                    count = len(News.objects.filter(ocatid=ocatid))  # for count news

                    b = Cat.objects.get(pk=ocatid)  # for count news
                    b.count = count  # for count news
                    b.save()  # for count news

                    return redirect('news_list')
                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)
                    error = "Your File Is Bigger Than 5 MB"
                    return render(request, 'back/error.html', {'error': error})

            else:
                fs = FileSystemStorage()
                fs.delete(filename)
                error = "Your File Not Supported"
                return render(request, 'back/error.html', {'error': error})

        except:
            error = "Please Input Your Image"
            return render(request, 'back/error.html', {'error': error})

    return render(request, 'back/news_add.html', {'cat': cat})
def news_delete(request, pk):
    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        a = News.objects.get(pk=pk).writer
        if str(a) != str(request.user):
            error = "Access Denied"
            return render(request, 'back/error.html', {'error': error})
    # -# Masteruser Access End #-#

    try:
        b = News.objects.get(pk=pk)

        fs = FileSystemStorage()
        fs.delete(b.picname)

        ocatid = News.objects.get(pk=pk).ocatid

        b.delete()

        count = len(News.objects.filter(ocatid=ocatid))

        m = Cat.objects.get(pk=ocatid)
        m.count = count
        m.save()


    except:
        error = "Something Wrong"
        return render(request, 'back/error.html', {'error': error})

    return redirect('news_list')
def news_edit(request, pk):
    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    if len(News.objects.filter(pk=pk)) == 0:
        error = "News Not Found"
        return render(request, 'back/error.html', {'error': error})
    perm = 0
    for i in request.user.groups.all():
        if i.name == "masteruser": perm = 1

    if perm == 0:
        a = News.objects.get(pk=pk).writer
        if str(a) != str(request.user):
            error = "Access Denied"
            return render(request, 'back/error.html', {'error': error})

    news = News.objects.get(pk=pk)

    cat = SubCat.objects.all()
    if request.method == 'POST':
        newstitle = request.POST.get('newstitle')  #
        newscat = request.POST.get('newscat')  #
        newstxtshort = request.POST.get('newstxtshort')  #
        newstxt = request.POST.get('newstxt')  #
        newsid = request.POST.get('newscat')  #

        tag = request.POST.get('tag')  ### This query for tag field

        if newstitle == "" or newstxtshort == "" or newstxt == "" or newscat == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error': error})

        try:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            url = fs.url(filename)
            if str(myfile.content_type).startswith("image"):
                if myfile.size < 5000000:  ## Check File Size ##
                    newsname = SubCat.objects.get(pk=newsid).name  # query
                    b = News.objects.get(pk=pk)
                    ##-## Old image deleting Code Start ##-##
                    fss = FileSystemStorage()
                    fss.delete(b.picname)
                    ##-## Old image deleting Code End ##-##
                    b.name = newstitle
                    b.short_txt = newstxtshort
                    b.body_txt = newstxt
                    b.picname = filename
                    b.picurl = url
                    b.catname = newsname
                    b.catid = newsid
                    b.tag = tag  ### This query for tag
                    b.act = 0
                    b.save()
                    return redirect('news_list')
                else:
                    fs = FileSystemStorage()
                    fs.delete(filename)
                    error = "Your File Is Bigger Than 5 MB"
                    return render(request, 'back/error.html', {'error': error})
            else:
                fs = FileSystemStorage()
                fs.delete(filename)
                error = "Your File Not Supported"
                #return render(request, 'error(html), {'error': error})
        except:
            newsname = SubCat.objects.get(pk=newsid).name  # query
            b = News.objects.get(pk=pk)
            b.name = newstitle
            b.short_txt = newstxtshort
            b.body_txt = newstxt
            b.catname = newsname
            b.catid = newsid
            b.tag = tag  ### This query for tag
            b.save()
            return redirect('news_list')
    ## take it from news add section and edit it End ##

    return render(request, '#html_file',
                  {'pk': pk, 'news': news, 'cat': cat})  # by using dictionary we send into template
def news_publish(request, pk):
    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End
    news = News.objects.get(pk=pk)
    news.act = 1
    news.save()
    return redirect('news_list')
def trending_add(request):
    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    if request.method == 'POST':
        txt = request.POST.get('txt')
        if txt == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error':error})
        b = Trending(txt=txt)
        b.save()
    trendinglist = Trending.objects.all()
    return render(request, 'back/trending.html', {'trendinglist':trendinglist})
def trending_del(request, pk):
    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End
    b = Trending.objects.filter(pk=pk)
    b.delete()
    return redirect('trending_add')
def trending_edit(request, pk):
    mytxt = Trending.objects.get(pk=pk).txt
    if request.method == 'POST':
        txt = request.POST.get('txt')
        if txt == "" :
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error':error})
        b = Trending.objects.get(pk=pk)
        b.txt = txt
        b.save()
        return redirect('trending_add')
    return render(request, 'back/trending_edit.html', {'mytxt':mytxt, 'pk':pk})
def subcat_list(request):
    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End
    subcat = SubCat.objects.all()
    return render(request, 'back/subcat_list.html', {'subcat': subcat})
def subcat_add(request):
    # Login check Start
    if not request.user.is_authenticated:
        return redirect('mylogin')
    # Login check End
    cat = Cat.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        catid = request.POST.get('cat')
        if name == "":
            error = "All Fields Required"
            return render(request, 'back/error.html', {'error': error})
        #### Check category exist or not Start ####
        if len(SubCat.objects.filter(name=name)) != 0:
            error = "This Name Used Before"
            return render(request, 'back/error.html', {'error': error})
        catname = Cat.objects.get(pk=catid).name
        b = SubCat(name=name, catname=catname, catid=catid)
        b.save()
        return redirect('subcat_list')
    return render(request, 'back/subcat_add.html', {'cat': cat})
def add_news_admin(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # For now, you can remove the redirect
            # return redirect('blog_list')  # Redirect to the blog list view
    else:
        form = NewsForm()

    return render(request, 'back/news_back_add.html', {'form': form})

def news_article_list(request):
    # Retrieve all news articles
    news_articles = NewsArticle.objects.all().order_by('-pk')

    return render(request, 'newsarticlelist.html', {'news_articles': news_articles})

def news_add_back(request):
    return render(request, 'add_news_article_back.html')

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
