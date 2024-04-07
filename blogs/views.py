from django.shortcuts import render,redirect
from .models import *
from django.shortcuts import render
from django.views import View
from django.contrib import messages

class BlogList(View):
    def get(self, request):
        blogs = Blog.objects.all()
        comments = Comment.objects.filter(approved=True)
        
        from django.core.paginator import Paginator
        p = Paginator(blogs, 9)
        page = self.request.GET.get('page')
        blogs_list = p.get_page(page)

        return render(request, 'front/blog.html', {'blogs': blogs_list, 'comments':comments})

class blog_detail(View):
    def get(self, *args, **kwargs):
        blog_id = self.kwargs['blog_id']
        blog = Blog.objects.get(id=blog_id)
        recent_blogs = Blog.objects.all().order_by('-pk')[:4]
        comments = blog.comment_set.filter(approved=True)[:12]  # Assuming you've set related_name='comment_set' in the Comment model
        return render(self.request, 'front/blog_detail.html', {'blog': blog,'recent_blogs':recent_blogs, 'comments': comments})
    
    def post(self, *args, **kwargs):
        blog = Blog.objects.get(id = self.kwargs['blog_id'])
        data = self.request.POST
        co = Comment.objects.create(blog =blog, author = data['author'], email = data['email'], message = data['message'])
        messages.success(self.request, "Successfully commented!")
        return redirect("blog_detail", blog_id= blog.id)
     
