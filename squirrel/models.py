
from django.db import models

from django.utils.translation import gettext as _

class Sighting(models.Model):
    latitude = models.FloatField(
        help_text = _('Latitude of the sighting'),
    )

    longitude = models.FloatField(
        help_text = _('Longitude of the sighting'),
    )

    unique_squirrel_id = models.CharField(
        max_length=20,
        unique=True,
        help_text = _('The unique id of squirrel(Format:Hectare-Shift-Date-Hectare Squirrel Number)'),
    )
    
    AM='AM'
    PM='PM'
    SHIFT_CHOICES = [
        (PM,_('PM')),
        (AM,_('AM')),
    ]

    shift = models.CharField(
        max_length=5,
        help_text = _('Shift'),
        choices = SHIFT_CHOICES,
    )

    date= models.DateField(
        help_text = _('Format:mmddyyyy'),
    )

    ADULT='Adult'
    JUVENILE='Juvenile'
    UNKNOWN='?'

    AGE_CHOICES=[
            (ADULT,_('Adult')),
            (JUVENILE,_('Juvenile')),
            (UNKNOWN,_('Unknown')),
    ]

    age = models.CharField(
        max_length=10,
        help_text = _('Age of squirrel'),
        choices=AGE_CHOICES,
        blank = True,
    )

    BLACK='Black'
    CINNAMON='Cinnamon'
    GRAY='Gray'

    PRI_FUR_COLOR_CHOICES=[
        (BLACK,_('Black')),
        (CINNAMON,_('Cinnamon')),
        (GRAY,_('Gray')),
    ]

    primary_fur_color = models.CharField(
        max_length=10,
        help_text = _('Primary Fur Color'),
        choices=PRI_FUR_COLOR_CHOICES,
        blank = True,
    )

    ABOVE_GROUND='Above Ground'
    GROUND_PLANE='Ground Plane'

    LOCATION_CHOICES=[
        (ABOVE_GROUND,_('Above Ground')),
        (GROUND_PLANE,_('Ground Plance')),
    ]

    location = models.CharField(
        max_length=20,
        help_text = _('Location of squirrel'),
        choices=LOCATION_CHOICES,
        blank = True,
    )

    specific_location = models.TextField(
        help_text = _('Specific Location'),
        blank = True,
    )

    running = models.BooleanField(
        help_text = _('Whether or not the squirrel is running'),
    )

    chasing = models.BooleanField(
        help_text = _('Whether or not the squirrel is chasing'),
    )

    climbing = models.BooleanField(
        help_text = _('Whether or not the squirrel is climbing'),
    )

    eating = models.BooleanField(
        help_text = _('Whether or not the squirrel is eating'),
    )

    foraging = models.BooleanField(
        help_text = _('Whether or not the squirrel is foraging'),
    )

    other_activities = models.TextField(
        help_text = _('Other activities the squirrel is doing'),
        blank = True,
    )

    kuks = models.BooleanField(
        help_text = _('Whether or not the squirrel kuks'),
    )

    quaas = models.BooleanField(
        help_text = _('Whether or not the squirrel quaas'),
    )

    moans = models.BooleanField(
        help_text = _('Whether or not the squirrel moans'),
    )

    tail_flags = models.BooleanField(
        help_text = _('Whether or not its tail flags'),
    )

    tail_twitches = models.BooleanField(
        help_text = _('Whether or not its tail twitches'),
    )

    approaches = models.BooleanField(
        help_text = _('Whether or not the squirrel approaches'),
    )


    indifferent = models.BooleanField(
        help_text = _('Whether or not the squirrel is indifferent'),
    )

    runs_from = models.BooleanField(
        help_text = _('Whether or not the squirrel runs from you'),
    )

    def __str__(self):
        return self.unique_squirrel_id
    
class Meta:
    managed = True
    



# Create your models here.
