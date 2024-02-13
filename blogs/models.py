from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=[('Nature', 'Nature'), ('Sports', 'Sports'), ('Food', 'Food'), ('Travel', 'Travel'), ('Fashion', 'Fashion'), ('Beauty', 'Beauty')])
    author = models.CharField(max_length=255)
    author_email = models.EmailField()
    publish_date = models.DateField()
    publish_time = models.TimeField()
    published_status = models.CharField(max_length=20, choices=[('Published', 'Published'), ('Hold', 'Hold')])
    content = models.TextField()
    blog_type = models.CharField(max_length=10, choices=[('Free', 'Free'), ('Paid', 'Paid')])
    images = models.ImageField(upload_to='blog_images/')

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(blank=True)
    message = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.blog.title}'

