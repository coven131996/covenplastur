from django.conf.urls import url
from django.urls import include
from . import views


urlpatterns = [
   
    url(r'^$', views.index, name='index'), 
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^authors/$', views.AuthorListView.as_view(), name='authors'),
   
]