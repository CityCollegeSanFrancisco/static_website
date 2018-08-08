from django.shortcuts import render

# Create your views here.

from .models import Contributor, Editor, Post, Tag

def index(request):
    """
    View function for home page of site
    """

    # ? create a loop of recent posts?
    # ? display the title, lead image, and preview of each?

    return render(request, 'index.html') # need context parameter?

