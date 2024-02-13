from django.shortcuts import render,redirect
from .models import *
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from .forms import BlogForm
def blog_list_admin(request):
    blogs = Blog.objects.all()
    return render(request, 'blog_list_admin.html', {'blogs': blogs})

def blog_detail(request, blog_id):
    # try:
        blog = Blog.objects.get(id=blog_id)
        comments = blog.comment_set.all()  # Assuming you've set related_name='comment_set' in the Comment model
        return render(request, 'front/blog_detail.html', {'blog': blog, 'comments': comments})
    
def add_comment(request, blog_id):
    if request.method == 'POST':
        blog = get_object_or_404(Blog, pk=blog_id)
        author = request.POST.get('author')
        email = request.POST.get('email')
        website = request.POST.get('website')
        message = request.POST.get('message')
        parent_id = request.POST.get('parent_id')  # If it's a reply, get the parent comment ID
        parent_comment = None
        if parent_id:
            parent_comment = get_object_or_404(Comment, pk=parent_id)
        comment = Comment.objects.create(blog=blog, author=author, email=email, website=website, message=message, parent=parent_comment)
        return redirect('blog_detail', blog_id=blog_id)
    else:
        return redirect('blog_list')  # Redirect to blog list page if not a POST request
def add_reply(request, comment_id):
    if request.method == 'POST':
        comment = get_object_or_404(Comment, pk=comment_id)
        author = request.POST.get('author')
        email = request.POST.get('email')
        website = request.POST.get('website')
        message = request.POST.get('message')
        reply = Comment.objects.create(author=author, email=email, website=website, message=message, parent=comment)
        return redirect('blog_detail', blog_id=comment.blog.pk)
    else:
        return redirect('blog_list')

def delete_blog(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)  # Retrieve the Blog object

    if request.method == 'POST':
        blog.delete()  # Delete the Blog object
        return redirect('blog_list_admin')  # Redirect to the blog list view

    context = {
        'blog': blog,
    }
    return render(request, 'delete_blog.html', context)  # Render the delete_blog.html template 

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'front/blog.html', {'blogs': blogs})

def Blogs_add(request):
    return render(request, 'add_blogs.html')
