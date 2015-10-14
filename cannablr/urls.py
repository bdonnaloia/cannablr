from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.views.generic import TemplateView
from accounts.views import home
from accounts.views import storefront
from accounts.views import get_entry
from accounts.views import show_reviews
from django.contrib import admin
from accounts.views import profile_listview
from accounts.views import EntryAPI
# admin.autodiscover()



urlpatterns = patterns('',
	url(r"^$", home),
	url(r"^storefront/", storefront),
	url(r"^sell/", get_entry),
    url(r"^reviews/(?P<username1>\w+)/$", show_reviews),
    # Examples:
    # url(r'^$', 'tester.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^accounts/(?P<username>[\@\.\w-]+)/listview/$', profile_listview),
    (r'^accounts/', include('userena.urls')),
    (r'^messages/', include('django_messages.urls')),
    (r'^api/storefront/$', EntryAPI),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
