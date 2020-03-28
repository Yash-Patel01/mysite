from django.shortcuts import render
from .models import course, registration, contact, blog1, comment2, coursecomment
from django.contrib.auth.models import User
from django.http import HttpResponse
import datetime
import urbandictionary as ud
from mysite.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

def index(request):
    # word = str(input('Enter the word :'))
    cour = course.objects.all()
    # defs = ud.define(word)
    # # rand = ud.random()
    # for i in defs:
    #     print(i.definition)
    return render(request, 'index.html', {'cour': cour})

def blog(request):
    blogg = blog1.objects.all()
    return render(request, "blog.html", {'blogg': blogg})


def contect1(request):

    return render(request, "contact.html")


def course1(request, id):
    course_id1 = ''
    user_id11 = ''
    user_id1 = ''
    count1 = 'y'
    current_user = request.user
    registration1 = registration.objects.filter(user_id=current_user.id, course_id=id)
    registration2 = registration.objects.all()
    for i in registration2:
        user_id2 = i.user_id
        course_id2 = i.course_id
    for i in registration1:
        user_id11 = i.user_id
        # course_id1  = i.course_id
        # print(course_id1)
        # print(user_id1)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        id = request.POST['id']
        Comment = coursecomment(name=name, email=email,
                                message=message, idofcourse=id)
        Comment.save()
    Comment = coursecomment.objects.all()
    Count = coursecomment.objects.filter(idofcourse=id).count()
    cour = course.objects.get(id=id)

    return render(request, 'course.html', {'cour': cour, 'comment': Comment,'count1': count1,'count': Count, 'registration1': registration1, 'registration2': registration2, 'user_id11': user_id11})


def message(request):
    id1 = ''
    if request.method == 'POST':
        id1 = request.POST['id']
        contact.objects.filter(id=id1).delete()

    mes = contact.objects.all()

    return render(request, 'message.html', {'mes': mes})


def contect11(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        Contect = contact(name=name, email=email,
                          subject=subject, message=message)
        Contect.save()
        return render(request, "contact.html")


def addblog(request):

    if request.method == 'POST':
        title = request.POST['title']
        name = request.POST['name']
        blog = request.POST['blog']
        datetime.date.today()
        # username = request.user.get_short_name()
        Blog = blog1(title=title, name=name, blog=blog)
        Blog.save()

        return render(request, "addblog.html")
    else:
        return render(request, "addblog.html")


def blogpost(request, blog):

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        id = request.POST['id']
        Comment = comment2(name=name, email=email,
                           message=message, idofblog=id)
        Comment.save()

    blogg = blog1.objects.get(id=blog)
    Count = comment2.objects.filter(idofblog=blog).count()
    comment = comment2.objects.all()

    return render(request, 'blog-post.html', {"blog": blogg, "comment": comment, 'count': Count})


def search(request):
    name = ''
    if request.method == 'POST':
        name = request.POST['name']
    search1 = User.objects.filter(first_name=name)
    return render(request, 'search.html', {'search': search1})


def register1(request, id11):
    id1 = ''
    id2 = id11
    user1 = ''
    email = ''
    if request.method == 'POST':
        id1 = request.POST['id']
        course_id = id2
        status = True
        user1 = User.objects.filter(id=id1)
        for i in user1:
            username = i.username
            first_name = i.first_name
            last_name = i.last_name
            email = i.email
            is_staff = i.is_staff
            user_id = i.id
        if not registration.objects.filter(user_id=user_id, username=username, first_name=first_name,last_name=last_name, email=email, is_staff=is_staff, course_id=course_id, status=status).exists():
            Registration = registration(user_id=user_id, username=username, first_name=first_name,last_name=last_name, email=email, is_staff=is_staff, course_id=course_id, status=status)
            Registration.save()
        current_user = request.user
        registration1 = registration.objects.filter(user_id=current_user.id)
        for i in registration1:
            email = i.email
        subject = 'Welcome to Edusite'
        course_details = course.objects.filter(id=id2)
        for i in course_details:
            title = i.title
            name = i.name 
            start_date = i.startdate
            end_date = i.enddate
        message ='''Dear Subscriber,

        
        I am Yash Kathrotiya. You are Enrolled in Edusite Course , Please check the Enrollment status in course page . hope you will enjoye the course tutorial which will be given by Edusite ...

        '''
        message1 = message + '\n\t Name of the course is : '+ title 
        message2 = message1 + '\n\t Name of the Faculty is : '+ name
        message4 = message2 + '\n\t Starting Date is : '+ str(start_date)
        message5 = message4 + '\n\t Ending Date is :  '+str(end_date)
        message3 = message5 + " \n\n\t\t***** DO NOT REPLY ON THIS EMAIL*****"
        recepient = email
        # print(message3)
        send_mail(subject,message3, EMAIL_HOST_USER, [recepient],fail_silently = False)
        print("****************************** SUCCESS ******************************")
            # return render(request, 'index.html')
        return render(request, "register1.html")
    else:
        print('course_id :'+id2)
        return render(request, 'register1.html', {'course_id': id2})



def dictionary(request):
    yash =''
    word =''
    if request.method == 'POST':
        word = request.POST['word']
        yash =ud.define(word)
        
    return render(request,'dictionary.html',{'word':yash,'word1':word})
