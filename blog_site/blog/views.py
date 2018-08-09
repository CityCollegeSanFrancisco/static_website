from django.shortcuts import render
from django.views import generic

# Create your views here.

from .models import Contributor, Editor, Post, Tag

def index(request):
    """
    View function for home page of site
    """

    # ? create a loop of recent posts?
    # ? display the title, lead image, and preview of each?

    return render(request, 'index.html') # need context parameter?

class PostListView(generic.ListView):
    model = Post
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(PostListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        #context['some_data'] = 'This is just some data'
        return context

class PostDetailView(generic.DetailView):
    model = Post
