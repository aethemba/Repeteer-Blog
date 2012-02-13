from django import template
from django.db.models import get_model
from blog.models import Entry

#Django custom tags:
#1 Read template contents (can be anything in string form)
#2 Parse string and look for tags and variables
#3 Call compilation function for each tag, it has two arguments 1) parser 2) contents of tag
#4 Return django.template.Node class (or sub-class)
#Result is a list of Node instances, which is the thing that will be rendered for output. (each Node has
#render() function)

#Compilation function
def do_latest_content(parser, token):
    #Split token.content to provide tag arguments
    bits = token.contents.split()
    if len(bits) != 5: 
        raise template.TemplateSyntaxError('get_latest_content tag takes exactly four arguments')
    #Split content_type (blog.models) into 'app' and 'model'
    model_args = bits[1].split('.')
    if len(model_args) != 2:
        raise template.TemplateSyntaxError("First argument to 'get_latest_content' must app.model string")
    #Get_model('app', 'model') --> e.g. ('blog', 'entry') or ('blog', 'link')
    #Use position arguments (model_args[0], model_args[1], etc) 
    model = get_model(*model_args)
    if model is None:
        raise template.TemplateSyntaxError("Not a valid model in 'get_latest_content' tag function")
    #bits[2] is model, bits[3] is 'as', bits[4] is tag variable name
    #get_latest_content blog.entry 5 as latest_entries
    return LatestContentNode(model,bits[2],bits[4])

class LatestContentNode(template.Node):
    def __init__(self, model, numberItems, varname):
        self.model = model
	self.num = int(numberItems)
	self.varname = varname

    def render(self, context):
        #Use the default manager of a model (e.g.,not Entry.objects.all but Entry.live.all)
	context[self.varname] = self.model._default_manager.all()[:self.num]
        return ''

register = template.Library()
register.tag('get_latest_content', do_latest_content)
