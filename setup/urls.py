from django.conf.urls import patterns, url

from setup import views

urlpatterns = patterns('',
    # ex: /setup/
    url(r'^$', views.index, name='index'),
)
