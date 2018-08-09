# Define models Contributor, Editor, Post, Tag

from django.db import models
from django.urls import reverse


class Contributor(models.Model):
    """
    Model representing a contributor to a post
    """
    #uniqueId = models.CharField(max_length=20, help_text='ID')
    first_name = models.CharField(max_length=20, help_text='first name')
    last_name = models.CharField(max_length=20, help_text='last name')

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('contributer-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.).
        """
        return self.first_name + ' ' + self.last_name 


class Editor(models.Model):
    """
    Model representing an editor of a post
    """
    #uniqueId = models.CharField(max_length=20, help_text='ID')
    first_name = models.CharField(max_length=20, help_text='first ame')
    last_name = models.CharField(max_length=20, help_text='last name')

    def get_absolute_url(self):
        """
        Returns the url to access a particular instance of MyModelName.
        """
        return reverse('Editor-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.).
        """
        return self.first_name + ' ' + self.last_name 


class Tag(models.Model):
    """
    Model representing tags for posts to organize by topic, programming language etc
    """
    name = models.CharField(max_length=20, help_text='Add a keyword to tag the post for easy discovery, e.g.\'Python\', \'Game Analysis\',etc')

    def __str__(self):
        """
	String for representing the MyModelName object (in Admin site etc.).
	"""
        return self.name


class Post(models.Model):
    """
    Model representing a blog post. A post can have multiple contributors and editors.
    Every post has 
	- at least one tag to organize by topic, programming language etc
	- a title/headline, 
	- a dek (a one-sentence summary/subhead displayed above the text), 
	- text, 
	- code (iframe from repl or just code; this can be inserted somewhere in the text),
	- a lead image to go at the top
	- other optional images
	- pull quote(s) (excerpts displayed on the page in a larger font style)

    """

    #uniqueId = models.CharField(max_length=20, help_text='ID')
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
    tags = models.ManyToManyField(Tag)

    #class Meta: (is this right?)
    ordering = ['-updated']

    def display_contributors(self):
        """
        Create a string for contributors to be displayed in admin
        """
        return ' and '.join((contributor.first_name + ' ' + contributor.last_name) for contributor in self.contributor.all()[:2])
    
    display_contributors.short_description = 'Contributors'

    def display_tags(self):
        """
        Create a string to show all tags for the post (future: as links to tag pages)
        """
        return ' | '.join(tag.name for tag in self.tags.all())

    def get_absolute_url(self):
         """Returns the url to access a particular instance of MyModelName."""
         return reverse('post-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.title



