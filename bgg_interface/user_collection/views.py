from django.shortcuts import render
from django.http import HttpResponse
from .forms import CollectionForm
from .services import ApiService

# Using a class-based genric view especially for rendering forms
from django.views.generic.edit import FormView
from django.views.generic import ListView, TemplateView

class SearchView(FormView):
  template_name = 'index.html'
  form_class = CollectionForm

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
    def collection(self): #NOTE that it's the method name that becomes the property on 'view'
      games = ApiService.get_collection(username=self.request.GET.get('username'))
      print("games", games)
      return games

    def message(self):
      test = {"header": "this is really cool!"}
      return test

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
