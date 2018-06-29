from django.shortcuts import render
from django.http import HttpResponse
from .forms import CollectionForm
from .services import ApiService

# Using a class-based genric view especially for rendering forms
from django.views.generic.edit import FormView
from django.views.generic import ListView, TemplateView
from django.urls import reverse_lazy

class SearchView(FormView):
  template_name = 'index.html'
  form_class = CollectionForm
  success_url = reverse_lazy('collection') # or just '/list/'?
  # or stay here with 'user_collection'?

# No model needed for the API data, but need to override the get_conetxt_data method if you want to use a built-in class-based view (Can't do this at all with ListView, etc, which need a model/db to interact with (?))

class CollectionView(TemplateView):
    template_name = 'collection_list.html'

    # Don't need to do this any more, it seems!
    # def get_context_data(self, **kwargs):
    #   # Call the base implementation first to get a context
    #   context = super().get_context_data(**kwargs)
    #   # Get the data from the API
    #   search_results = form.search()
    #   # Add in a QuerySet of the collection data
    #   context['collection'] = search_results
    #   return context
    # Because now you can define values that become props of a new 'view' object in the template
    # https://reinout.vanrees.org/weblog/2014/05/19/context.html
    def collection(self):
      collection = ApiService.get_collection()
      return collection



# Hand-rolled way, without class-based view
# def index(request):
#   search_results = {}
#   # if this is a POST request we need to process the form data
#   if request.method == 'POST':
#       # create a form instance and populate it with data from the request:
#       form = CollectionForm(request.POST) #Why do this?
#       # check whether it's valid:
#       if form.is_valid():
#           # process the data in form.cleaned_data as required
#           # ...
#           print("searching for collection XXXXXXX")
#           search_results = form.search()
#           # or shoud we redirect to a new URL:
#           # return HttpResponseRedirect('user_collection/collection/')

#   # if a GET (or any other method) we'll create a blank form
#   else:
#     form = CollectionForm()

#   return render(request, 'index.html', {'form': form, 'search_results': search_results })

# def collection(request):
#   print("collection?", request)
#   return HttpResponse("We made it to the collection page!")
