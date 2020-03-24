from django.shortcuts import render
from mysite.settings import EMAIL_HOST_USER
from project.models import registration
from django.contrib.auth.models import User
from . import forms
from django.core.mail import send_mail
# Create your views here.
#DataFlair #Send Email
# def subscribe(request):
#     current_user = request.user
#     email = ''
#     registration1 = registration.objects.filter(user_id=current_user.id)
#     for i in registration1:
#         email = i.email
#     print("user email is recived")
#     print(email)
#     # if request.method == 'POST':
#         # sub = forms.Subscribe(request.POST)
#     subject = 'Welcome to Edusite'
#     message = 'Dear Student , You are Enrolled in Edusite Course , Please check the Enrollment status in course page . hope you will enjoye the course tutorial which will be given by Edusite ...'
#     recepient = email
#     send_mail(subject,message, EMAIL_HOST_USER, [recepient],fail_silently = False)
#     print("****************************** SUCCESS ******************************")
#     return render(request, 'index.html')