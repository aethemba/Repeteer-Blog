from django.contrib.auth.models import User
from django.db import models
from tagging.fields import TagField
from markdown import markdown
from django.conf import settings #Import settings file
import datetime

class Category(models.Model):
   title = models.CharField(max_length=250, help_text='Max. 250 characters')
   slug = models.SlugField(unique=True)
   description = models.TextField()

   class Admin:
       pass

   class Meta:
       ordering = ['title']
       verbose_name_plural= 'Categories'

   def __unicode__(self):
       return self.title

   def get_absolute_url(self):
       return "/categories/%s/" % self.slug


class Entry(models.Model):
   LIVE_STATUS = 1
   DRAFT_STATUS = 2
   HIDDEN_STATUS = 3
   STATUS_CHOICES = (
       (LIVE_STATUS, 'Live'),
       (DRAFT_STATUS, 'Draft'),
       (HIDDEN_STATUS, 'Hidden')
   )
   
   title = models.CharField(max_length=250)
   excerpt = models.TextField(blank=True)
   body = models.TextField()
   pub_date = models.DateTimeField(default=datetime.datetime.now)
   slug = models.SlugField(unique_for_date='pub_date')
   author = models.ForeignKey(User)
   enable_comments = models.BooleanField(default=True)
   featured = models.BooleanField(default=False)
   status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE_STATUS)
   categories = models.ManyToManyField(Category)

   tags = TagField()

   excerpt_html = models.TextField(editable=False, blank=True)
   body_html = 	models.TextField(editable=False, blank=True)

   #Define custom save method to add HTML markup once at saving
   def save(self):
      self.body_html = markdown(self.body)
      if self.excerpt:
          self.excerpt_html = markdown(self.excerpt)
      super(Entry, self).save()

   class Meta:
      verbose_name_plural = 'Entries'
      ordering = ['-pub_date']

   #This doesn't seem to work. I still need to register the model at the admin.py file
   class Admin:
      pass

   def __unicode__(self):
      return self.title

   def get_absolute_url(self):
      #Function returns: the url name (defined in urls.py), a tuple of positional arguments, a dictionary with keyword arguments
      return ('blog_entry_detail', (), {'year': self.pub_date.strftime("%Y"), 'month': self.pub_date.strftime("%b").lower(), 'day': self.pub_date.strftime("%d"), 'slug': self.slug})
   #decorator causes a 'reverse lookup. Uses regexp from url to create the correct url string and fills in the proper values for arguments required in the url'
   get_absolute_url = models.permalink(get_absolute_url)

class Link(models.Model):
    title = models.CharField(max_length=250)
    desciption = models.TextField(blank=True)
    desciption_html = models.TextField(blank=True)
    #Django verifies the url by doing a HTTP request. verify_exists can override this behavior
    url = models.URLField(unique=True)

    posted_by = models.ForeignKey(User)
    
    #Declaring a function runs it only once. A function as an argument gets called every time, giving the real date
    pub_date = models.DateTimeField(default=datetime.datetime.now)
    slug = models.SlugField(unique_for_date='pub_date')

    tags = TagField()

    enable_comments = models.BooleanField(default=True)
    post_elsewhere = models.BooleanField('Post to Twitter', default=False)

    via_name = models.CharField('Via', max_length=250, blank=True, help_text='Person name which site')
    via_url = models.URLField('Via URL', blank=True, help_text='URL of site where you spotted the link')

    class Meta:
        ordering = ['pub_date']

    class Admin:
        pass

    def __unicode__(self):
        return self.title

    def save(self):
        if self.description:
	    self.decription_html = markdown(self.description)
        super(Link, self).save()

    def get_absolute_url(self):
        return ('blog_link_detail', (), {'year':self.pub_date.strftime("Y%"), 'month':self.pub_date.strftime("%b").lower(), 'day':self.pub_date.strftime("%d"), 'slug': self.slug})
    get_absolute_url = models.permalink(get_absolute_url)


