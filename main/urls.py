from django.conf.urls import patterns, url

urlpatterns = patterns('',

    # Static pages
    url(r'^$', 'main.views.index', name='main'),
    ) 
