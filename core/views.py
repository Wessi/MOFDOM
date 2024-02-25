from django.shortcuts import render, redirect
from django.views import View 
from.models import ContactUs
import threading
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, send_mail
from django.contrib import messages
from core.models import Settings

class Contact(View):
    def get (self, *args, **kwargs):
        map = Settings.objects.first().map_link
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


class AccountVerifiedThread(threading.Thread):
    def __init__(self, data, request):
        self.data = data 
        self.request= request
        threading.Thread.__init__(self) 


    def run(self):
        try:
            current_site = get_current_site(self.request)
            mail_subject = 'Your Medstore account is verified.'
            message = render_to_string('email/accounts/account_validated.html', {
                'user': self.user,
                'domain': current_site.domain,
            })
            to_email = self.user.email
            email = EmailMultiAlternatives(mail_subject, message, "Kanenus", [to_email],)
            email.attach_alternative(message, 'text/html')
            email = email.send()
            print(f"sent account verified email to {self.user.email}", email)
            return (True, "sent email" ) 
        
        except Exception as e:
            print("Email Exception ", e)
            return (False, e)
