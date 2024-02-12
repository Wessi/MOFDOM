from django.shortcuts import render, redirect
from django.views import View 
import threading
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives, send_mail


class ContactUs(View):
    def post(self, *args, **kwargs):
        data = self.request.POST
        msg = f"A visitor called {data['name']} with a phone number of {data['phone']} has sent a message with a subject of {data['subject']}. \n {data['message']}"
        e = send_mail(f"Visitor message : {data['subject']}", msg, from_email="Kanenus", recipient_list=['info@kanenustechnologies.com'], fail_silently=False)
        print(e)
        return redirect("index")         


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
