from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from SprinklerStudio import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SprinklerStudio.views.home', name='home'),
    # url(r'^SprinklerStudio/', include('SprinklerStudio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^weather/', include('weather.urls')),
    url(r'^sprinklers/', include('sprinklers.urls')),
    url(r'^setup/', include('setup.urls')),
    url(r'^$', views.index, name='index')
)
