from django.conf.urls.defaults import *
from blog.models import Entry

entry_info_dict = {
    'queryset': Entry.live.all(),
    'date_field' : 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
    #Url gets regexp, a generic view, a variable for the generic view, and a name to be used by a view
    #The arguments for for the generic view are all in the url (yearh, month, day)
    url(r'^$', 'archive_index', entry_info_dict, 'blog_entry_archive_index'),
    url(r'^(?P<year>\d{4})/$', 'archive_year', entry_info_dict, 'blog_entry_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'archive_month', entry_info_dict, 'blog_entry_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'archive_day', entry_info_dict, 'blog_entry_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', entry_info_dict, 'blog_entry_detail'),
)
