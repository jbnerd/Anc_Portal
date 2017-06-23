from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib import auth
from django.db import IntegrityError
from django.contrib.auth.models import User
import json
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, BadHeaderError
from django.conf import settings
from .forms import *
import random
from django.template import loader

cancel_order_pin = 123654

def index(request):
	return render(request, 'anc/index.html')

def email(request):
	try:
		send_mail('Test', 'Test', settings.EMAIL_HOST_USER, ['abhivjoshi.aj@gmail.com'], fail_silently = False)
	except BadHeaderError:
		return HttpResponse('Invalid Header Found')

	return HttpResponse('Seems to have worked fine')

@login_required
def login(request):
	try :
		user = request.user
		up = UserProfile()

		up.user = user
		up.save()
	except IntegrityError:
		return redirect('/inform')
	
	return redirect('/inform')

@login_required
def inform(request):
	try:
		user = request.user
		up = UserProfile.objects.get(user = user)
	except:
		raise Http404('Something went wrong.')

	if up.login == 0:
		if request.POST:
			form = InitialForm(request.POST)
			if form.is_valid():
				data = form.cleaned_data

				up.login = 1
				up.phone = data['phone']
				up.secret_pin = data['secret_pin']
				up.save()

				html_message = loader.render_to_string(
					'anc/message2.html',
					{'order':order, 'up':up}
				)

				try:
					send_mail('ANC Portal Registration', 'Pin and details', settings.EMAIL_HOST_USER, [user.email], fail_silently = False, html_message = html_message)
				except BadHeaderError:
					return HttpResponse('Invalid Header Found')

			return redirect('/order')

		else:
			form = InitialForm()
			return render(request, 'anc/inform.html', {'form':form, 'up': up})
	else :
		return redirect('/order')

@login_required
def order(request):
	
	if request.POST:
		form = OrderForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data

			try:
				up = UserProfile.objects.get(user = request.user)
				order = Order()
			except:
				raise Http404('Awww... man.')

			order.user = up.user
			order.key = up.key
			
			order.item1 = Item.objects.get(name = data['item1'])
			order.quantity1 = data['quantity1']

			order.item2 = Item.objects.get(name = data['item2'])
			order.quantity2 = data['quantity2']

			order.item3 = Item.objects.get(name = data['item3'])
			order.quantity3 = data['quantity3']

			order.item4 = Item.objects.get(name = data['item4'])
			order.quantity4 = data['quantity4']

			order.item5 = Item.objects.get(name = data['item5'])
			order.quantity5 = data['quantity5']

			if order.quantity1 is not None :
				order.total += int(order.item1.price)*int(order.quantity1)
			else:
				return HttpResponse('You haven\'t selected any item, go back and select one or hit the cancel button')

			if order.quantity2 is not None :
				order.total += int(order.item2.price)*int(order.quantity2)
			if order.quantity3 is not None :
				order.total += int(order.item3.price)*int(order.quantity3)
			if order.quantity4 is not None :
				order.total += int(order.item4.price)*int(order.quantity4)
			if order.quantity5 is not None :
				order.total += int(order.item5.price)*int(order.quantity5)

			order.save()

			return redirect('/place_order')
		else:
			return HttpResponse('There was some unfortunate error')


	else:
		form = OrderForm()
		items = Item.objects.all()
		up = UserProfile.objects.get(user = request.user)
		return render(request, 'anc/order.html', {'form':form, 'items' : items, 'up' : up})

@login_required
def place_order(request):
	user = request.user
	up = UserProfile.objects.get(user = user)
	try:
		order = Order.objects.get(user = request.user, key = up.key)
	except MultipleObjectsReturned:
		up.key += 1
		up.save()
		return HttpResponse('Please have patience and click on the submit order button only once. Go back and try again')

	if order.ordered == 0:
		order.ordered = 1

		num = "%0.6d" % random.randint(0, 999999)
		order.num = num

		order.save()
	
		up.key += 1
		up.save()

		html_message = loader.render_to_string(
			'anc/message.html',
			{'order':order, 'up':up}
		)

		try:
			send_mail('ANC Order reference pin - ' + str(num), 'Bill', settings.EMAIL_HOST_USER, [user.email], fail_silently = False, html_message = html_message)
		except BadHeaderError:
			return HttpResponse('Invalid Header Found')

		return render(request, 'anc/thanks.html', {'order':order, 'up':up})

	else:
		return HttpResponse('This order has already been placed.')

def test(request):
	if request.user.is_authenticated():
		return HttpResponse("WElcome  http://ancportal.herokuapp.com/logout")
	else:
		return HttpResponse("http://ancportal.herokuapp.com/soc/login/google-oauth2/?next=/login/")

@login_required
def user_logout(request):
	auth.logout(request)
	return redirect('/')

def unbilled(request):
	orders = Order.objects.filter(user = request.user, ordered = 1)
	up = UserProfile.objects.get(user = request.user)
	return render(request, 'anc/incomplete.html', {'orders' : orders, 'up' : up})

def billed(request):
	orders = Order.objects.filter(user = request.user, ordered = 2)
	up = UserProfile.objects.get(user = request.user)
	return render(request, 'anc/complete.html', {'orders' : orders, 'up' : up})

def print_screen(request):
	return render(request, 'anc/first.html')

def cancel_order(request):
	if request.POST:
		form = CancelForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data

			ref_no = data['ref_no']
			secret_pin = data['secret_pin']
			try:
				order = Order.objects.get(num = ref_no)
			except:
				return HttpResponse('Order doesn\'t exist')

			user = authenticate(username = 'anc_operator', password = secret_pin)
			if user.is_active:
				order.ordered = 1
				order.save()
				return render(request, 'anc/first.html')
			else:
				return HttpResponse('Something went wrong.')

		else:
			return HttpResponse('There was some error in the form fields. Please try again')
	else:
		form = CancelForm()
		return render(request, 'anc/cancel.html', {'form' : form})

def print_order(request):
	if request.POST:
		form = PrintForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data

			ref_no = data['ref_no']
			try:
				order = Order.objects.get(num = ref_no)
			except:
				return HttpResponse('Order doesn\'t exist')

			secret_pin = data['secret_pin']
			try:
				up = UserProfile.objects.get(user = order.user)
			except:
				return HttpResponse('The required user does not exists. Please contact the authority.')

			if secret_pin == up.secret_pin:
				order.ordered = 2
				order.save()
				return render(request, 'anc/printpaper.html', {'order' : order})
			else:
				return HttpResponse('Either of the reference number or the entered pin is wrong')

		else:
			return HttpResponse('There was some error in the form fields. Please try again')
	else:
		form = PrintForm()
		return render(request, 'anc/print.html', {'form' : form})