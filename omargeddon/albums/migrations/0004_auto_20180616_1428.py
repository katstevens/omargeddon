# Generated by Django 2.0.6 on 2018-06-16 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_auto_20180616_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrackCredit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credit', models.CharField(blank=True, max_length=256, null=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.Album')),
                ('contributor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.Personnel')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='albums.Track')),
            ],
        ),
        migrations.RemoveField(
            model_name='albumcredit',
            name='album',
        ),
        migrations.RemoveField(
            model_name='albumcredit',
            name='contributor',
        ),
        migrations.DeleteModel(
            name='AlbumCredit',
        ),
    ]
