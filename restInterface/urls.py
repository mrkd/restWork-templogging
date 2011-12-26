from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('restInterface.views',
    url(r'^$', 'index'),
    url(r'^sensor_(?P<s>\d+)-temp_(?P<t>\d+)-datetime_(?P<d>\d+)/$','insert'),
    url(r'^msg/(?P<msg>.+)/$','processMsg'),

    # Examples:
    # url(r'^$', 'leeHouseSite.views.home', name='home'),
    # url(r'^leeHouseSite/', include('leeHouseSite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)