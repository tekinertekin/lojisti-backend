from django.db import models
from django.conf import settings


class Options:
    CREATED = "CREATED"
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    ACCEPTED = "ACCEPTED"
    CANCELLED = "CANCELLED"

    PUBLICATION_STATUS = (
        (CREATED, "CREATED"),
        (PENDING, "PENDING"),
        (ACTIVE, "ACTIVE"),
        (ACCEPTED, "ACCEPTED"),
        (CANCELLED, "CANCELLED"),
    )

class LojistiBaseModel(models.Model):

    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_createdby', on_delete=models.DO_NOTHING)
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='%(class)s_modifiedby', null=True, blank=True, on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True


class Point(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()

class Country(models.Model):
    name = models.CharField(max_length=100)

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, related_name="country_city", blank=False, null=False, on_delete=models.DO_NOTHING)

class Town(models.Model):
    name = models.CharField(max_length=100)
    city =  models.ForeignKey(City, related_name="city_town", blank=False, null=False, on_delete=models.DO_NOTHING)

class District(models.Model):
    name = models.CharField(max_length=100)
    town = models.ForeignKey(Town, related_name="town_district", blank=False, null=False, on_delete=models.DO_NOTHING)


class Address(models.Model):
    district = models.ForeignKey(District, related_name="district_address", blank=False, null=False, on_delete=models.DO_NOTHING)
    avenue = models.CharField(max_length=100) #cadde
    street = models.CharField(max_length=100) #sokak
    building_number = models.CharField(max_length=20)
    floor = models.IntegerField(blank=True, null=True)
    door_number = models.CharField(max_length=20)
    
class Location(models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address, related_name="address_location", blank=True, null=True, on_delete=models.DO_NOTHING)
    point = models.ForeignKey(Point, related_name="point_location", blank=True, null=True, on_delete=models.DO_NOTHING)
