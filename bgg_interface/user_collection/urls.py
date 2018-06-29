from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
  path('', views.SearchView.as_view(), name="index"),
  url(r'list/$', views.CollectionView.as_view(), name="collection")
]


