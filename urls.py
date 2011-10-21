from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.shortcuts import render

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'www.views.home', name='home'),
    # url(r'^www/', include('www.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.urls')),
    url(r'^blog/', include('diario.urls.entries')),
    url(r'^author/', include('diario.urls.entries_by_author')), 
    url(r'^$', view=render, name='mainpage', kwargs={
					'template_name': 'mainpage.html'}),
#    url(r'^forum/', include('vlfa.urls.categories')),
#    url(r'^forum/', include('vlfa.urls.topics')),
#    url(r'^forum/', include('vlfa.urls.posts')),
)

if settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
