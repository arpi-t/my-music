from django.conf.urls import patterns, include, url
from django.contrib import admin
from songs_scrapper.views import HomeView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', HomeView.as_view(), name='home_view'),
)


