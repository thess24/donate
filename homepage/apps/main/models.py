from django.db import models
from django.forms import ModelForm, Textarea
from django import forms
from django.contrib.auth.models import User


class List(models.Model):
	ICON_LIST = (
		('glyphicon-arrow-up', 'Arrow Up'), 
		('glyphicon-asterisk', 'Asterisk'),
		('glyphicon-bell', 'Bell'),
		('glyphicon-book', 'Book'),
		('glyphicon-briefcase', 'Briefcase'),
		('glyphicon-calendar', 'Calendar'),
		('glyphicon-check', 'Checklist'),
		('glyphicon-cutlery', 'Silverware'),
		('glyphicon-earphone', 'Phone'),
		('glyphicon-envelope', 'Mail'),
		('glyphicon-euro', 'Euro'),
		('glyphicon-film', 'Film'),
		('glyphicon-fire', 'Fire'),
		('glyphicon-flash', 'Lightning Bolt'),
		('glyphicon-heart', 'Heart'),
		('glyphicon-music', 'Music'),
		('glyphicon-plane', 'Plane'),
		('glyphicon-search', 'search'),
		('glyphicon-shopping-cart', 'Shopping Cart'),
		('glyphicon-usd', 'US Dollar'),
		('glyphicon-trash', 'Trash'),
		)
	name = models.CharField(max_length=500)
	user = models.ForeignKey(User)
	date = models.DateTimeField(auto_now_add=True)
	icon = models.CharField(max_length=500, choices=ICON_LIST,blank=True)
#  add color, styling options
#  pinned, aka sticky
#  secret or visible-password to view
	def __unicode__(self):
		return self.name


class Item(models.Model):
	listfk = models.ForeignKey(List)
	text = models.CharField(max_length=500)
	complete = models.BooleanField()
	completed_time = models.DateTimeField(null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	url = models.URLField(blank=True, null=True)

	def __unicode__(self):
		return self.text




##########    FORMS   ############



class ListForm(ModelForm):
	class Meta:
		model = List
		exclude = ['user', 'date']


class ItemForm(ModelForm):
	class Meta:
		model = Item
		exclude = ['date', 'complete', 'completed_time']