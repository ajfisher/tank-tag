from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url("^$", "tanks.views.phonecontrol"),
    url("^tanks", include('tanks.urls')),
    url("", include("django_socketio.urls")),
)
