# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollectionPoint',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Naam')),
            ],
            options={
                'verbose_name_plural': 'Afhaalpunten',
                'verbose_name': 'Afhaalpunt',
            },
        ),
        migrations.CreateModel(
            name='Cooperant',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100, verbose_name='Voornaam')),
                ('last_name', models.CharField(max_length=100, verbose_name='Achternaam')),
                ('phone', models.CharField(max_length=100, verbose_name='Telefoon')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('code', models.CharField(max_length=100, verbose_name='Code')),
                ('street_and_number', models.CharField(max_length=100, verbose_name='Straat + nummer')),
                ('zip_code', models.PositiveIntegerField(verbose_name='Postcode')),
                ('city', models.CharField(max_length=100, verbose_name='Stad')),
            ],
            options={
                'verbose_name_plural': 'Coöperanten',
                'verbose_name': 'Coöperant',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Naam')),
                ('weight', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Gewicht')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=4, verbose_name='Prijs')),
            ],
            options={
                'verbose_name_plural': 'Pakketten',
                'verbose_name': 'Pakket',
            },
        ),
        migrations.CreateModel(
            name='WeeklySubscription',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Afhaaldatum')),
                ('amount', models.PositiveIntegerField(default=1, verbose_name='Aantal')),
                ('is_paid', models.BooleanField(default=False, verbose_name='Betaald')),
                ('collection_point', models.ForeignKey(to='subscriptions.CollectionPoint', verbose_name='Afhaalpunt')),
                ('cooperant', models.ForeignKey(to='subscriptions.Cooperant', related_name='subscription_set', verbose_name='Coöperant')),
                ('subscription_type', models.ForeignKey(to='subscriptions.SubscriptionType', verbose_name='Pakket')),
            ],
            options={
                'verbose_name_plural': 'Inschrijvingen',
                'verbose_name': 'Inschrijving',
            },
        ),
    ]
