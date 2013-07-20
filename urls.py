from django.conf.urls.defaults import patterns, include, url
from rest_framework import routers
from testApp import views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'temperatureReadings', views.TemperatureReadingViewSet)

urlpatterns = patterns('',
    url(r'^restInterface/', include('restInterface.urls')),
    url(r'^status/', include('status.urls')),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
    # Examples:
    url(r'^$', 'home_page.views.index'),


    url(r'^api/', include(router.urls)),
    url(r'^temperatureReadingsList/$', 'snippet_list'),
    url(r'^temperatureReadings/(?P<pk>[0-9]+)/$', 'snippet_detail'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # url(r'^leeHouseSite/', include('leeHouseSite.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
