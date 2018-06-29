from django.urls import path
from . import views

urlpatterns = [
  path('', views.SearchView.as_view(), name="index"),
  path('list/', views.CollectionView.as_view(), name="collection")
]


