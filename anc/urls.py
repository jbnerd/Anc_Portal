from django.conf.urls import url
from anc import views

app_name = 'anc'

urlpatterns = [
	#/
	url(r'^$', views.index, name='index'),
	
	#logout/
	url(r'^logout/$', views.user_logout, name='logout'),
	
	#test/
	url(r'^test/', views.test, name = 'test'),

	#email/
	url(r'^email/', views.email, name = 'email'),

	#inform/
	url(r'^inform/', views.inform, name = 'inform'),

	#order/
	url(r'^order/', views.order, name = 'order'),

	#place_order/
	url(r'^place_order/', views.place_order, name = 'place_order'),

	#login/
	url(r'^login/', views.login, name = 'login'),

	#unbilled/
	url(r'^unbilled/', views.unbilled, name = 'unbilled'),

	#billed/
	url(r'billed/', views.billed, name = 'billed'),

	#print_screen/
	url(r'print_screen/', views.print_screen, name = 'print_screen'),

	#cancel_order/
	url(r'cancel_order/', views.cancel_order, name = 'cancel_order'),

	#print_order/
	url(r'print_order/', views.print_order, name = 'print_order'),

]