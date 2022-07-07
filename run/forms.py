from django import forms
from run.models import Person

class PersonsForm(forms.ModelForm):
    class Meta:
        models = Person
        fields = '__all__'

