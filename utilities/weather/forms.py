from django.forms import ModelForm, TextInput
from weather.models import CityName

class CityForm(ModelForm):
    class Meta:
        model = CityName
        fields = ['name']
        widgets = {'name' : TextInput(attrs={'class':'input', 'placeholder':'City Name'})}
