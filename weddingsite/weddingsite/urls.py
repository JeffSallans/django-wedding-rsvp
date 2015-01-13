from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'weddingsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'rsvp.views.index', name = 'home'),
    url(r'^getrsvp$', 'rsvp.views.get_rsvp_page'),
    url(r'^saversvp$', 'rsvp.views.save_rsvp'),
    url(r'^getall$', 'rsvp.views.get_all_rsvp'),
    url(r'^admin/', include(admin.site.urls)),
)
