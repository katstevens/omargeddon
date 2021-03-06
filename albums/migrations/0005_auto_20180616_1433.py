# Generated by Django 2.0.6 on 2018-06-16 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0004_auto_20180616_1428'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='trackcredit',
            name='album',
        ),
        migrations.AddField(
            model_name='album',
            name='tags',
            field=models.ManyToManyField(related_name='album_tags', to='albums.Tag'),
        ),
        migrations.AddField(
            model_name='track',
            name='tags',
            field=models.ManyToManyField(related_name='track_tags', to='albums.Tag'),
        ),
    ]
