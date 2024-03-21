from django.db import models

class NewsCategory(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
    def get_list_fields():
        return ['name']
    
    list_fields = get_list_fields()

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    content = models.TextField()
    featured_image = models.ImageField(upload_to='news_images/')
    minutes_read = models.IntegerField()
    likes = models.IntegerField(default=0)
    news_category = models.ForeignKey(NewsCategory, on_delete = models.SET_NULL, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)
        
    def __str__(self):
        return self.title
    
    def category(self):
        return self.news_category if self.news_category else ""
    
    def get_list_fields():
        return ['title', 'author', 'minutes_read', 'news_category', 'created_at']
    
    list_fields = get_list_fields()
