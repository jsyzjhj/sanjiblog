from django.conf.urls import url
from . import views

app_name='blog'
urlpatterns = [
    url(r'^$',views.mainpage,name='mainpage'),
    url(r'^mainpage.html',views.mainpage,name='forget'),
    url(r'^post/(?P<pk>[0-9]+)/$',views.post,name='post'),
    #url(r'^$',views.index,name='index'),
    #url(r'^post/(?P<pk>[0-9]+)/$',views.detail,name='detail'),
    url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$', views.archives, name='archives'),
    url(r'^category/(?P<pk>[0-9]+)/$',views.category,name='category'),
    url(r'about.html',views.about,name='about'),
    url(r'post/(?P<pk>[0-9]+)/like',views.like,name='like')

]
