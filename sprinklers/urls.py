from django.conf.urls import patterns, url

from sprinklers import views

urlpatterns = patterns('',
    # ex: /sprinklers/
    url(r'^$', views.index, name='index'),
    # ex: /sprinklers/5/
    url(r'^(?P<sprinkler_id>\d+)/$', views.detail, name='detail'),
    # ex: /sprinkler/5/on/
    url(r'^(?P<sprinkler_id>\d+)/on/$', views.on, name='on'),
    # ex: /sprinkler/5/off/
    url(r'^(?P<sprinkler_id>\d+)/off/$', views.off, name='off'),
    # ex: /sprinkler/5/status/
    url(r'^(?P<sprinkler_id>\d+)/status/$', views.status, name='status'),
)
