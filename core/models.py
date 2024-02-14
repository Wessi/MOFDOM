from django.db import models

class ContactUs(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    sent_date =models.DateField( auto_now_add = True )

    def __str__(self):
        return f"Message from : {self.full_name}"
    
    class Meta:
        ordering = ('-id',)



    
