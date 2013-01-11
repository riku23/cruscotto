from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cruscotto_proj.views.home', name='home'),
    # url(r'^cruscotto_proj/', include('cruscotto_proj.foo.urls')),
    (r'^verifica/', include('cruscotto.urls.verifica')),
    (r'^check/', include('sitescheck.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
