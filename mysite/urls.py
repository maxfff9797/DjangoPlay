
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from mysite.views import hello,current_datetime,hours_ahead
admin.autodiscover()

urlpatterns = [
    url(r'^hello/$', hello),
    url(r'^time/$',current_datetime),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^admin/',include('admin.site.urls')),
]
