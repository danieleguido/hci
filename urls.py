from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
	url(r'^$', 'dime_shs.hci.views.index', name='index'),	
)