from django.db import models
from django.urls import reverse

class Editor(models.Model):
    uniqueId = model.CharField((max_length=20, help_text='ID')
    first_name = model.CharField((max_length=20, help_text='first ame')
    last_name = model.CharField((max_length=20, help_text='last name')
    #posts = 
    def get_absolute_url(self):
         """Returns the url to access a particular instance of MyModelName."""
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.field_name


###########

class Contributor(models.Model):
    uniqueId = model.CharField((max_length=20, help_text='ID')
    first_name = model.CharField((max_length=20, help_text='first name')
    last_name = model.CharField((max_length=20, help_text='last name')
    #posts = 
    #tags = 
    def get_absolute_url(self):
         """Returns the url to access a particular instance of MyModelName."""
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.first_name + ' ' + self.last_name 

###########

class Post(models.Model)
    uniqueId = model.CharField((max_length=20, help_text='ID')
    title = model.CharField((max_length=50, help_text='title')
    #contributor = choices??
       #design so that editors can add and choose from a list of contributors
    #editor
    updated = model.DateField(auto_now=True)
    dek = model.CharField((max_length=50, help_text='summarize your post in one sentence')
    text = model.TextField((help_text='text')
    code = model.CharField((help_text='enter code or repl iframe')
    lead_image = model.ImageField
    images = model.ImageField
    pull_quotes = model.CharField((help_text='pull quote')
    tags = model.ManyToManyField

    #class Meta: (is this right?)
    ordering = ['-updated']
    def get_absolute_url(self):
         """Returns the url to access a particular instance of MyModelName."""
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title

###########

class Tag
    name = model.CharField((max_length=20, help_text='ID')
    #posts = 

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.name

