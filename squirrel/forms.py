from django.forms import ModelForm

from .models import Sighting         #8.16, import AdoptRequest, which is cousin class

class SightingRequestForm(ModelForm):
    class Meta:
        model = Sighting
        fields = '__all__'
