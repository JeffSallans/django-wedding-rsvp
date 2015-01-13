# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Household',
            fields=[
                ('id_household', models.IntegerField(serialize=False, primary_key=True)),
                ('address_number', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id_person', models.IntegerField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rsvp',
            fields=[
                ('id_rsvp', models.IntegerField(serialize=False, primary_key=True)),
                ('max_count', models.IntegerField()),
                ('count', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('last_modified', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='household',
            name='person',
            field=models.ForeignKey(to='rsvp.Person'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='household',
            name='rsvp',
            field=models.ForeignKey(to='rsvp.Rsvp'),
            preserve_default=True,
        ),
    ]
