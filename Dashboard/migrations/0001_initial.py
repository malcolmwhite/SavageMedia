# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('created_on', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FlightDate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('campaign', models.ForeignKey(to='dashboard.Campaign')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialMediaAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('handle', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialMediaService',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('icon', models.ImageField(upload_to=b'')),
                ('post_name', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TargetGraph',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('central_user', models.TextField()),
                ('depth', models.IntegerField()),
                ('campaigns', models.ManyToManyField(to='dashboard.Campaign')),
                ('services', models.ManyToManyField(to='dashboard.SocialMediaService')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TargetPhrase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phrase', models.TextField()),
                ('campaigns', models.ManyToManyField(to='dashboard.Campaign')),
                ('services', models.ManyToManyField(to='dashboard.SocialMediaService')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='socialmediaaccount',
            name='service',
            field=models.ForeignKey(to='dashboard.SocialMediaService'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='accounts_liked',
            field=models.ManyToManyField(to='dashboard.SocialMediaAccount'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='campaign',
            name='created_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
