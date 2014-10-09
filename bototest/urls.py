from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bototest.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^home/', TemplateView.as_view(template_name="home.html"), name="home"),
    url(r'^upload/getcsv/$', 'upload.views.getcsv', name="getcsv"),
    url(r'^display/files/$', 'display.views.files', name="files")
    url(r'^display)dispdata/(?P<csvx_id>\d+)/$', 'display.views.dispdata', name="dispdata"),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
