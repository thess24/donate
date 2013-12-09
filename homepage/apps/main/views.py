# Create your views here.
from django.shortcuts import render, get_object_or_404
from apps.main.models import Sponsor, Charity, Raffle, Entry, EntryForm, CharityImage, RaffleLevel, UserExtend, CreateRaffleForm, RaffleImage
import datetime
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
import stripe
from django.db.models import Sum


def index(request):

	return render(request, 'main/index.html', )
 
def about(request): 

	return render(request, 'main/about.html', )

def contact(request): 

	return render(request, 'main/about.html', )

@login_required()
def myaccount(request): 

	return render(request, 'main/myaccount.html', )

def raffle(request, raffle):
	raffleobject = Raffle.objects.get(slug__iexact=raffle)
	levels = RaffleLevel.objects.filter(raffle=raffleobject)
	try:extuser = UserExtend.objects.get(user=request.user)
	except:extuser={} 
	entries = Entry.objects.filter(user=request.user, raffle=raffleobject).aggregate(Sum('count'))

	if request.method=='POST':
		if 'addentry' in request.POST:
			form = EntryForm(extuser, request.POST)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.user = request.user
				instance.raffle = raffleobject

				extuser.tickets = extuser.tickets - instance.count
				extuser.save()

				instance.save()

				return HttpResponseRedirect(reverse('apps.main.views.raffle', args=(raffle,)))

	else: form = EntryForm(extuser)


	context= {'raffle':raffleobject, 'levels':levels, 'form':form, 'entries':entries }
	return render(request, 'main/raffle.html', context)

def createraffle(request):
	extuser = UserExtend.objects.get(user=request.user)

	if request.method=='POST':
		if 'createraffle' in request.POST:
			form = CreateRaffleForm(request.POST)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.user = request.user
				instance.raffle = raffleobject
				instance.save()

				context= {'form':form}
				return render(request, 'main/createraffle.html', context)

	else: form = CreateRaffleForm()


	context= {'form':form }
	return render(request, 'main/createraffle.html', context)

def currentraffles(request):

	raffleobjects = Raffle.objects.filter(active=True).order_by('expiretime')

	context= {'raffle':raffleobjects}
	return render(request, 'main/currentraffles.html', context)


def tickets(request):


	if request.method == 'POST':
		stripe.api_key = "sk_test_ChZBYMHbZLagr8DQdsqxcq9y"

		# Get the credit card details submitted by the form
		token = request.POST['stripeToken']
		tickets = int(request.POST['ticketnumber'])
		ticektscents = tickets*100

		# Create the charge on Stripe's servers - this will charge the user's card
		try:
		  charge = stripe.Charge.create(
		      amount=ticektscents, # amount in cents, again
		      currency="usd",
		      card=token,
		      description="payinguser@example.com"
		  )
		except stripe.CardError, e:
			# The card has been declined
			raise Http404

		extuser = UserExtend.objects.get(user=request.user)
		extuser.tickets = extuser.tickets + tickets
		extuser.save()
		return HttpResponseRedirect(reverse('apps.main.views.tickets', args=()))

	return render(request, 'main/tickets.html')
	
# @login_required() 
# def list(request):
# 	lists = List.objects.filter(user=request.user)
# 	items = Item.objects.filter(listfk__user = request.user)

# 	if request.method=='POST':
# 		if 'add' in request.POST:
# 			form = ListForm(request.POST)
# 			if form.is_valid():
# 				instance = form.save(commit=False)
# 				instance.user = request.user
# 				instance.save()
# 				return HttpResponseRedirect(reverse('apps.main.views.list', args=()))

# 	else: form = ListForm()

# 	context= {'lists':lists, 'items':items, 'form':form}
# 	return render(request, 'main/list.html', context)
