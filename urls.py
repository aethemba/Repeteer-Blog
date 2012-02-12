from django.conf.urls.defaults import *
from blog.models import Entry, Link

entry_info_dict = {
    'queryset' : Entry.objects.all(),
    'date_field' : 'pub_date',
}

link_info_dict = {
    'queryset': Link.objects.all(),
    'date_field': 'pub_date',
}

urlpatterns = patterns('django.views.generic.date_based',
    #Url gets regexp, a generic view, a variable for the generic view, and a name to be used by a view
    #The arguments for for the generic view are all in the url (yearh, month, day)
    url(r'^$', 'archive_index', entry_info_dict, 'blog_entry_archive_index'),
    url(r'^(?P<year>\d{4})/$', 'archive_year', entry_info_dict, 'blog_entry_archive_year'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/$', 'archive_month', entry_info_dict, 'blog_entry_archive_month'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'archive_day', entry_info_dict, 'blog_entry_archive_day'),
    url(r'^(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', entry_info_dict, 'blog_entry_detail'),

   url(r'^links/$', 'archive_index', link_info_dict, 'blog_link_archive_index'),
   url(r'^links/(?P<year>\d{4})/$', 'archive_year', link_info_dict, 'blog_lonk_archive_year'),
   url(r'^links/(?P<year>\d{4})/(?P<month>\w{3})/$','archive_month', link_info_dict, 'blog_link_archive_month'),
   url(r'^links/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/$', 'archive_day', link_info_dict, 'blog_link_archive_day'),
   url(r'^links/(?P<year>\d{4})/(?P<month>\w{3})/(?P<day>\d{2})/(?P<slug>[-\w]+)/$', 'object_detail', link_info_dict, 'blog_link_detail'),

)

urlpattern += patterns('blog.views', 
   (r'^categories/$', 'category_list'),
   (r'^categories/(?P<slug>[-\w]+)/$', 'category_detail'),
)
