from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url("^$", "tanks.views.phonecontrol"),
    url("^tanks", include('tanks.urls')),
    url("", include("django_socketio.urls")),
    url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/favicon.ico'}),
)
