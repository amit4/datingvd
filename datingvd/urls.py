from django.conf.urls import patterns, include, url
from main import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'datingvd.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'datingvd.views.index', name='home'),
    url(r'^main/',include(main.site.urls)),
)
