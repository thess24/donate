# Create your views here.
from django.shortcuts import render, get_object_or_404
from apps.main.models import List, Item
import datetime
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.contrib.auth.decorators import login_required

@login_required() 
def index(request):
	lists = List.objects.filter(user=request.user)
	items = Item.objects.filter(listfk__user = request.user)

	if request.method=='POST':
		if 'delete' in request.POST:
			itemid = request.POST['id']
			Item.objects.get(id=itemid).delete()

		elif 'check' in request.POST:
			itemid = request.POST['id']
			item = Item.objects.get(id=itemid)
			item.complete = True
			item.completed_time = datetime.datetime.now()
			item.save()

		elif 'deletelist' in request.POST:
			listid = request.POST['id']
			List.objects.get(id=listid).delete()

	context= {'lists':lists, 'items':items}
	return render(request, 'main/index.html', context)


def list(request):
	lists = List.objects.filter(user=request.user)
	items = Item.objects.filter(listfk__user = request.user)

	if request.method=='POST':
		if 'add' in request.POST:
			pass

	context= {'lists':lists, 'items':items}
	return render(request, 'main/list.html', context)
