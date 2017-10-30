from django.conf.urls import include, url
from . import views


urlpatterns = [

	url(r'^$', views.index_page, name='index_page'),
	url(r'^cakes/$', views.cakes_page, name='cakes_page'),
	url(r'^cupcakes/$', views.cupcakes_page, name='cupcakes_page'),
	url(r'^desserts/$', views.desserts_page, name='desserts_page'),
	url(r'^healthy_treats/$', views.healthy_treats_page, name='healthy_treats_page'),
	url(r'^corporates/$', views.corporates_page, name='corporates_page'),
	url(r'^occasions/$', views.occasions_page, name='occasions_page'),
	url(r'^contact/$', views.contact_page, name='contact_page')
	]