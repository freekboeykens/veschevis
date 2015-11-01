# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cooperant',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('first_name', models.CharField(verbose_name='Voornaam', max_length=100)),
                ('last_name', models.CharField(verbose_name='Achternaam', max_length=100)),
                ('phone', models.CharField(verbose_name='Telefoon', max_length=100)),
                ('email', models.EmailField(verbose_name='E-mail', max_length=100)),
                ('code', models.CharField(verbose_name='Code', max_length=100)),
                ('street', models.CharField(verbose_name='Straat', max_length=100)),
                ('number', models.PositiveIntegerField(verbose_name='Nummer')),
                ('mailbox', models.CharField(verbose_name='Bus', max_length=5)),
                ('zip_code', models.PositiveIntegerField(verbose_name='Postcode')),
                ('city', models.CharField(verbose_name='Stad', max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Coöperanten',
                'verbose_name': 'Coöperant',
            },
        ),
    ]
