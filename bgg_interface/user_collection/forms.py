from django import forms

class CollectionForm(forms.Form):
  user_name = forms.CharField(label='Your BGG username', max_length=25)
