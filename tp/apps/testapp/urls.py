from django.conf.urls.defaults import *


urlpatterns = patterns('tp.apps.testapp.views',
    url(r'^$', 'index'),
)
