from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog', views.blog, name='blog'),
    path('contect1', views.contect1, name='contect1'),
    # path('register1',views.register1,name='register1'),
    path('message',views.message,name='message'),
    path('contect11', views.contect11, name='contect11'),
    path('addblog', views.addblog, name='addblog'),
    path('blogpost/<blog>', views.blogpost,name='blogpost'),
    path('course1/<id>', views.course1, name='course1'),
    path('search',views.search,name='search'),
    path('course1/enroll/register/<id11>',views.register1,name='course1/register'),
    path('Dictionary',views.dictionary,name='Dictionary'),

    # re_path('register',views.register1,name='register')

    
]



