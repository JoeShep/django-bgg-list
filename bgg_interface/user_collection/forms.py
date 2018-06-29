from django import forms

class CollectionForm(forms.Form):
  username = forms.CharField(label='Your BGG username', max_length=25)
