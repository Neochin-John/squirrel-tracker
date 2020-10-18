from django.forms import ModelForm, DateField, DateInput
from django.utils.translation import gettext as _

from .models import Sighting         #8.16, import AdoptRequest, which is cousin class

class SightingRequestForm(ModelForm):
    date = DateField(input_formats=["%m%d%Y"], help_text=_('Format:mmddyyyy'))
    class Meta:
        model = Sighting
        fields = '__all__'


class SightingUpdateForm(ModelForm):
    date = DateField(input_formats=["%m%d%Y"], help_text=_('Format:mmddyyyy'), widget=DateInput(format='%m%d%Y'),)
    class Meta:
        model = Sighting
        fields = ['latitude', 'longitude', 'unique_squirrel_id', 'shift', 'date', 'age']