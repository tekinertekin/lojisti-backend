from django.db import models
from util.models import LojistiBaseModel, Location, Options

class Publication(LojistiBaseModel):
    name = models.CharField(max_length=100)
    old_home = models.ForeignKey(Location, related_name="location_publication_old_home", blank=True, null=True, on_delete=models.DO_NOTHING)
    new_home = models.ForeignKey(Location, related_name="location_publication_new_home", blank=True, null=True, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=30, choices=Options.PUBLICATION_STATUS, default=Options.CREATED)

