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
	name = models.CharField(max_length=140)
	user = models.ForeignKey(User)
	date = models.DateTimeField(auto_now_add=True)
	icon = models.CharField(max_length=100, choices=ICON_LIST,blank=True)
	sticky = models.BooleanField()
	secret = models.BooleanField()

	def __unicode__(self):
		return self.name


class Item(models.Model):
	listfk = models.ForeignKey(List)
	title = models.CharField(max_length=140)
	complete = models.BooleanField()
	completed_time = models.DateTimeField(null=True, blank=True)
	date = models.DateTimeField(auto_now_add=True)
	url = models.URLField(blank=True, null=True)
	text = models.CharField(max_length=1000, blank=True, null=True)

	def __unicode__(self):
		return self.title



##########    FORMS   ############



class ListForm(ModelForm):
	class Meta:
		model = List
		exclude = ['user', 'date']


class ItemForm(ModelForm):
	class Meta:
		model = Item
		exclude = ['date', 'complete', 'completed_time']