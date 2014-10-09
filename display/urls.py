from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('display.views',
    url(r'^files/$', 'files', name="files"),
    url(r'^dispdata/(?P<csvx_id>\d+)/$', 'dispdata', name="dispdata"),
)