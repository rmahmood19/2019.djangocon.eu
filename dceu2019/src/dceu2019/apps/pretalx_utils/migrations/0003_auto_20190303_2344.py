# Generated by Django 2.1.4 on 2019-03-03 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pretalx_utils', '0002_auto_20190302_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talkextraproperties',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
