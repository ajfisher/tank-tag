from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('tanks.views',
    url(r"^/game$", 'showgame'),
    url(r"", 'phonecontrol'),
)
