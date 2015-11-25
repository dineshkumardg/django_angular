# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actor_id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'actor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('address', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50, null=True, blank=True)),
                ('district', models.CharField(max_length=20)),
                ('postal_code', models.CharField(max_length=10, null=True, blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('city_id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('city', models.CharField(max_length=50)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'city',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('country', models.CharField(max_length=50)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'country',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=50, null=True, blank=True)),
                ('active', models.IntegerField()),
                ('create_date', models.DateTimeField()),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'customer',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('film_id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
                ('release_year', models.TextField(null=True, blank=True)),
                ('rental_duration', models.IntegerField()),
                ('rental_rate', models.DecimalField(max_digits=4, decimal_places=2)),
                ('length', models.SmallIntegerField(null=True, blank=True)),
                ('replacement_cost', models.DecimalField(max_digits=5, decimal_places=2)),
                ('rating', models.CharField(max_length=5, null=True, blank=True)),
                ('special_features', models.CharField(max_length=54, null=True, blank=True)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'film',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FilmActor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'film_actor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FilmCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'film_category',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='FilmText',
            fields=[
                ('film_id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'db_table': 'film_text',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('inventory_id', models.AutoField(serialize=False, primary_key=True)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'inventory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('language_id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'language',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.SmallIntegerField(serialize=False, primary_key=True)),
                ('amount', models.DecimalField(max_digits=5, decimal_places=2)),
                ('payment_date', models.DateTimeField()),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'payment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('rental_id', models.AutoField(serialize=False, primary_key=True)),
                ('rental_date', models.DateTimeField()),
                ('return_date', models.DateTimeField(null=True, blank=True)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'rental',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('picture', models.TextField(null=True, blank=True)),
                ('email', models.CharField(max_length=50, null=True, blank=True)),
                ('active', models.IntegerField()),
                ('username', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=40, null=True, blank=True)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'staff',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('store_id', models.AutoField(serialize=False, primary_key=True)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'store',
                'managed': False,
            },
        ),
    ]
