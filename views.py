from django.shortcuts import get_object_or_404, render_to_response
from blog.models import Category

from django.views.generic.list_detail import object_list

#def entries_index(request):
#    return render_to_response('blog/entry_list.html', {'entry_list': Entry.objects.all()})

#Above view is no longer required because a generic view in the URLConf connects to the models

def category_detail(request):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/category_detail.html', 
                                            {'object_list': category.live_entry_set(),
					     'category': category})


