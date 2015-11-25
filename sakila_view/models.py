# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Actor(models.Model):
    actor_id = models.SmallIntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'actor'


class Address(models.Model):
    address_id = models.SmallIntegerField(primary_key=True)
    address = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50, blank=True, null=True)
    district = models.CharField(max_length=20)
    city = models.ForeignKey('City')
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=20)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'address'


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'category'


class City(models.Model):
    city_id = models.SmallIntegerField(primary_key=True)
    city = models.CharField(max_length=50)
    country = models.ForeignKey('Country')
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'city'


class Country(models.Model):
    country_id = models.SmallIntegerField(primary_key=True)
    country = models.CharField(max_length=50)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'country'


class Customer(models.Model):
    customer_id = models.SmallIntegerField(primary_key=True)
    store = models.ForeignKey('Store')
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.CharField(max_length=50, blank=True, null=True)
    address = models.ForeignKey(Address)
    active = models.IntegerField()
    create_date = models.DateTimeField()
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'customer'


class Film(models.Model):
    film_id = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.TextField(blank=True, null=True)  # This field type is a guess.
    language = models.ForeignKey('Language', related_name='film_language')
    original_language = models.ForeignKey('Language', blank=True, null=True)
    rental_duration = models.IntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.CharField(max_length=5, blank=True, null=True)
    special_features = models.CharField(max_length=54, blank=True, null=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film'


class FilmActor(models.Model):
    actor = models.ForeignKey(Actor)
    film = models.ForeignKey(Film)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film_actor'
        unique_together = ('actor', 'film')


class FilmCategory(models.Model):
    film = models.ForeignKey(Film)
    category = models.ForeignKey(Category)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film_category'
        unique_together = ('film', 'category')


class FilmText(models.Model):
    film_id = models.SmallIntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'film_text'


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film)
    store = models.ForeignKey('Store')
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'inventory'


class Language(models.Model):
    language_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'language'


class Payment(models.Model):
    payment_id = models.SmallIntegerField(primary_key=True)
    customer = models.ForeignKey(Customer)
    staff = models.ForeignKey('Staff')
    rental = models.ForeignKey('Rental', blank=True, null=True)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    payment_date = models.DateTimeField()
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'payment'


class Rental(models.Model):
    rental_id = models.AutoField(primary_key=True)
    rental_date = models.DateTimeField()
    inventory = models.ForeignKey(Inventory)
    customer = models.ForeignKey(Customer)
    return_date = models.DateTimeField(blank=True, null=True)
    staff = models.ForeignKey('Staff')
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rental'
        unique_together = ('rental_date', 'inventory', 'customer')


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    address = models.ForeignKey(Address)
    picture = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    store = models.ForeignKey('Store')
    active = models.IntegerField()
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=40, blank=True, null=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'staff'


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    manager_staff = models.ForeignKey(Staff, related_name='store_manager_staff', unique=True)
    address = models.ForeignKey(Address)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'store'
