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



# make newsletter work --mailchimp

# autopayment system for putting raffles online

# change raffle listing based on status (sponsored, recently expired, new, etc)
    # new, recently expired as methods on classes

# update user value on token buy, token use

# update entry value on token use

# figure out aggregated sum to give to charities, add in how much a users vote is worth

# user has to fill in info before progressing

# ability to make charity account, sponsor account

# currentraffles filter on state, hosted/non, enddate, startdate

# way to have links to raffle site in addition to hosted raffles

# make way to stop raffle and pick winner

# small raffle pics in scroller

# user maintaninence

# make contact page

# ability to list or host raffle

	# list - $5 per day
	# host- $10 per day
	# featured- add $50 per day
    # sponsored- add $5 per day