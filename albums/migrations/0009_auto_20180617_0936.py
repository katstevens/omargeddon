# Generated by Django 2.0.6 on 2018-06-17 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0008_auto_20180617_0936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='album_tags', to='albums.Tag'),
        ),
    ]
