from django.db import models

from django.db import models
from django.utils.translation import gettext as _

class Sighting(models.Model):
    latitude = models.FloatField(
        help_text = _('Latitude of the sighting'),
    )

    longitude = models.FloarField(
        help_text = _('Longitude of the sighting'),
    )

    unique_squirrel_id = models.CharField(
        help_text = _('Hectare-Shift-Date-Hectare Squirrel Number'),
    )

    SHIFT_CHOICES = [
        ('PM','PM'),
        ('AM','AM'),
    ]

    shift = models.CharField(
        help_text = _('Shift'),
        choices = SHIFT_CHOICES,
    )

    date= models.DateField(
        help_text = _('Date'),
    )

    age = models.CharField(
        help_text = _('Adult or Juvenile'),
        blank = True,
    )

    primary_fur_color = models.CharField(
        help_text = _('Primary Fur Color'),
        blank = True,
    )

    location = models.CharField(
        help_text = _('Ground Plane or Above Ground'),
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
        return self.squirrel_unique_id



# Create your models here.
