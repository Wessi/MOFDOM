from django.db import models

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=255)
    # category = models.CharField(max_length=100, null=True,
    #                             choices=[('Nature', 'Nature'), ('Sports', 'Sports'), ('Food', 'Food'), ('Travel', 'Travel'), ('Fashion', 'Fashion'), ('Beauty', 'Beauty')])
    blog_category = models.ForeignKey(BlogCategory, on_delete = models.SET_NULL, null=True)
    author = models.CharField(max_length=255)
    author_email = models.EmailField()
    publish_date = models.DateField()
    publish_time = models.TimeField()
    published_status = models.CharField(max_length=20, choices=[('Published', 'Published'), ('Hold', 'Hold')])
    content = models.TextField()
    blog_type = models.CharField(max_length=10, choices=[('Free', 'Free'), ('Paid', 'Paid')])
    images = models.ImageField(upload_to='blog_images/')

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return self.title
    
    def category(self):
        return self.blog_category if self.blog_category else ""
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True)
    message = models.TextField()
    approved = models.BooleanField(default=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-id",)

    def __str__(self):
        return f'Comment by {self.author} on {self.blog.title}'

class tweets(models.Model):
    tweet_id = models.CharField(max_length=250, null=True, blank=True)
    tweet_text = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.tweet_text
    
    class Meta:
        ordering = ("-id",)