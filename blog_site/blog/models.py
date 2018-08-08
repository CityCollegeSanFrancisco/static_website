# Define models Contributor, Editor, Post, Tag

from django.db import models
from django.urls import reverse

###########

class Contributor(models.Model):
    uniqueId = models.CharField(max_length=20, help_text='ID')
    first_name = models.CharField(max_length=20, help_text='first name')
    last_name = models.CharField(max_length=20, help_text='last name')
#    posts = models.ManyToManyField('Post') # use string for not-yet-defined parameter
#    tags = models.ManyToManyField('Tag')  # use string for not-yet-defined parameter

    def get_absolute_url(self):
         """Returns the url to access a particular instance of MyModelName."""
         return reverse('model-detail-view', args=[str(self.id)])
    
    #def __str__(self):
     #   """String for representing the MyModelName object (in Admin site etc.)."""
      #  return self.first_name + ' ' + self.last_name 

###########


class Editor(models.Model):
    uniqueId = models.CharField(max_length=20, help_text='ID')
    first_name = models.CharField(max_length=20, help_text='first ame')
    last_name = models.CharField(max_length=20, help_text='last name')
#    posts = models.ManyToManyField('Post') # use string for not-yet-defined parameter
#    tags = models.ManyToManyField('Tag')  # use string for not-yet-defined parameter
    def get_absolute_url(self):
         """Returns the url to access a particular instance of MyModelName."""
         return reverse('model-detail-view', args=[str(self.id)])
    
    #def __str__(self):
     #   """String for representing the MyModelName object (in Admin site etc.)."""
      #  return self.first_name + ' ' + self.last_name 

###########

class Post(models.Model):
    uniqueId = models.CharField(max_length=20, help_text='ID')
    title = models.CharField(max_length=50, help_text='title')
    contributor = models.ManyToManyField(Contributor, help_text='Select contributors')  
    #design so that editors can add and choose from a list of contributors
    editor = models.ManyToManyField(Editor)
    updated = models.DateField(auto_now=True)
    dek = models.CharField(max_length=50, help_text='summarize your post in one sentence')
    text = models.TextField(help_text='text')
    code = models.TextField(help_text='enter code or repl iframe')
    lead_image = models.ImageField
    images = models.ImageField
    pull_quotes = models.TextField(help_text='pull quote')
    tags = models.ManyToManyField

    #class Meta: (is this right?)
    ordering = ['-updated']
    def get_absolute_url(self):
         """Returns the url to access a particular instance of MyModelName."""
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title


###########


class Tag:
    name = models.CharField(max_length=20, help_text='ID')
    #posts = 

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name

