from django.shortcuts import get_object_or_404, render_to_response
from blog.models import Category

#def entries_index(request):
#    return render_to_response('blog/entry_list.html', {'entry_list': Entry.objects.all()})

#Above view is no longer required because a generic view in the URLConf connects to the models

def category_list(request):
    return render_to_response('blog/category_list.html', {'object_list': Category.objects.all()})

def category_detail(request):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('blog/category_detail.html', 
                                            {'object_list': category.entry_set.all(),
					     'category': category})

