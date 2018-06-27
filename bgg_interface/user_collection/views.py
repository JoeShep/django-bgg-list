from django.shortcuts import render
from django.http import HttpResponse
from .forms import CollectionForm

def index(request):
  search_results = {}
  # if this is a POST request we need to process the form data
  if request.method == 'POST':
      # create a form instance and populate it with data from the request:
      form = CollectionForm(request.POST) #Why do this?
      # check whether it's valid:
      if form.is_valid():
          # process the data in form.cleaned_data as required
          # ...
          print("searching for collection XXXXXXX")
          search_results = form.search()
          # or shoud we redirect to a new URL:
          # return HttpResponseRedirect('user_collection/collection/')

  # if a GET (or any other method) we'll create a blank form
  else:
    form = CollectionForm()

  return render(request, 'index.html', {'form': form, 'search_results': search_results })

# def collection(request):
#   print("collection?", request)
#   return HttpResponse("We made it to the collection page!")
