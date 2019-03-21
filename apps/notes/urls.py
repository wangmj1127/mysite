from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'note'
urlpatterns = [
    # homepage
    path(r'', views.index, name='index'),
    url(r'^edit_note/$', views.edit_note, name='edit_note'),
    url(r'^store_note/$', views.store_note, name='store_note'),
    url(r'^like_note$', views.like_note, name='like_note'),
    url(r'^note_detail/(?P<id>[0-9]+)/$', views.detail, name='note_detail'),
    url(r'^comment/$', views.comment, name='comment'),
    url(r'^wishlist/$', views.wishlist, name='wishlist'),
]
