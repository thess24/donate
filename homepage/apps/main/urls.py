from django.conf.urls import patterns, url
from apps.main import views
from settings.common import *
 

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^currentraffles/', views.currentraffles, name='currentraffles'),
    url(r'^tickets/', views.tickets, name='tickets'),
    url(r'^about/', views.about, name='about'),
    url(r'^createraffle/', views.createraffle, name='createraffle'),
    url(r'^myaccount/', views.myaccount, name='myaccount'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^(?P<raffle>.+)/$', views.raffle, name='raffle'),

    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': MEDIA_ROOT}),

)  





# user maintaninence

# fix entries count on raffle page

# make contact page

# show raffle when its time, remove shortly after expired

# fix submission with no tickets

# ability to list or host raffle

	# list - $5 per day
	# host- $10 per day
	# featured- add $10 per day