from django.db import models

# Create your models here.
class course(models.Model):

    title = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    img = models.ImageField(upload_to='pics')
    category = models.CharField(max_length=200)
    Premium = models.BooleanField(default=False)
    startdate = models.DateField(auto_now_add=False)
    enddate = models.DateField(auto_now_add=False)
    about = models.TextField()

class registration(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=50)  
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    is_staff = models.BooleanField(default=False)
    course_id = models.IntegerField()
    status = models.BooleanField(default=False)

class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=500)   

class blog1(models.Model):

    title = models.CharField(max_length=100)
    name  = models.CharField(max_length=50)
    blog = models.TextField()
    date =  models.DateField(auto_now_add=True)
    img = models.ImageField(upload_to='pics')

class comment2(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    date =  models.DateField(auto_now_add=True)
    idofblog = models.IntegerField()

class coursecomment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    date =  models.DateField(auto_now_add=True)
    idofcourse = models.IntegerField()

