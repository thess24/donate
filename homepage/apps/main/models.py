from django.db import models
from django.forms import ModelForm, Textarea
from django import forms
from django.contrib.auth.models import User
from localflavor.us.models import USStateField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field
from crispy_forms.bootstrap import StrictButton, PrependedText


class UserExtend(models.Model):
	user = models.OneToOneField(User)
	tickets = models.IntegerField()
	state = USStateField()

	def __unicode__(self):
		return self.user.username


class Sponsor(models.Model):
	name = models.CharField(max_length=140)
	image = models.ImageField(upload_to='sponsor')
	thumb = models.ImageField(upload_to='sponsorthumb')
	url = models.URLField()

	def __unicode__(self):
		return self.name


class Charity(models.Model):
	name = models.CharField(max_length=140)
	url = models.URLField()
	description = models.TextField()
	thumb = models.ImageField(upload_to='charitythumb')

	def __unicode__(self):
		return self.name


class CharityImage(models.Model):
	charity = models.ForeignKey(Charity)
	imagename = models.CharField(max_length=140)
	image = models.ImageField(upload_to='charity')

	def __unicode__(self):
		return self.charity.name


class Raffle(models.Model):
	title = models.CharField(max_length=140)
	starttime = models.DateTimeField()
	expiretime = models.DateTimeField()
	active = models.BooleanField()
	slug = models.SlugField()
	charity = models.ForeignKey(Charity)
	sponsor = models.ForeignKey(Sponsor)
	charitydesc = models.TextField()
	sponsordesc = models.TextField()
	gendesc = models.TextField()
	shortdesc = models.CharField(max_length=280)
	image = models.ImageField(upload_to='prize')
	state = USStateField()
	rules = models.TextField()
	maxtickets = models.IntegerField(blank=True)

	def __unicode__(self):
		return self.title


class RaffleLevel(models.Model):
	raffle = models.ForeignKey(Raffle)
	price = models.IntegerField()
	description = models.TextField()
	image = models.ImageField(upload_to='level')

	def __unicode__(self):
		return self.raffle.title


class RaffleImage(models.Model):
	raffle = models.ForeignKey(Raffle)
	imagename = models.CharField(max_length=140)
	image = models.ImageField(upload_to='raffle')

	def __unicode__(self):
		return self.raffle.title


class Entry(models.Model):
	raffle = models.ForeignKey(Raffle)
	user = models.ForeignKey(User)
	count = models.IntegerField()

	def __unicode__(self):
		return self.user.username


 
##########    FORMS   ############

class CreateRaffleForm(ModelForm):
	class Meta:
		model = Raffle
		exclude = ['slug', 'active']

	def __init__(self, *args, **kwargs):
		super(CreateRaffleForm, self).__init__(*args, **kwargs)
		self.helper= FormHelper()
		self.helper.form_class = 'form-horizontal'
		self.helper.label_class = 'col-lg-4'
		self.helper.field_class = 'col-lg-8'
		self.fields['expiretime'].label = "Date and Time Raffle will expire"
		self.fields['charitydesc'].label = "Charity Description"
		self.fields['sponsordesc'].label = "Sponsor Description"
		self.fields['gendesc'].label = " General Description of Raffle"
		self.fields['shortdesc'].label = " Short description to be displayed as a preview"
		self.fields['image'].label = "Image of item to be raffled"
		self.helper.layout = Layout(
				'title' ,
				'starttime' ,
				'expiretime' ,
				'active' ,
				'charity' ,
				'sponsor' ,
				'charitydesc',
				'sponsordesc', 
				'gendesc',
				'shortdesc',
				'image',
				'rules',
				'maxtickets',
		    StrictButton('Create Raffle', name='createraffle', type='submit',css_class='btn-primary btn-lg pull-right'),
		)
class EntryForm(ModelForm):
	class Meta:
		model = Entry
		exclude = ['raffle', 'user']

	def __init__(self,extuser,*args,**kwargs):
		self.extuser = extuser
		super(EntryForm, self).__init__(*args, **kwargs)

	def clean(self):
		cleaned_data = super(EntryForm, self).clean()
		if not cleaned_data.get('count'): raise forms.ValidationError('Enter a number of tickets')
		entries = int(cleaned_data.get('count'))
		try:tickets = self.extuser.tickets
		except: raise forms.ValidationError('You need tickets!')
		if entries > tickets: raise forms.ValidationError('You need more tickets!')
		


		return cleaned_data