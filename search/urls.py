from django.conf.urls import url
from . import views

app_name='search'
urlpatterns = [
    url(r'^$',views.index,name='index'),
    #url(r'^search-form/$', views.search_form,name='search_form'),
    url(r'^search/$', views.search,name='search')
]
