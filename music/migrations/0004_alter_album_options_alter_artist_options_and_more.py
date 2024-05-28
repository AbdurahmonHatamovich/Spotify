# Generated by Django 5.0.4 on 2024-05-14 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_alter_tracks_options_tracks_listened_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'ordering': ('id',)},
        ),
        migrations.AddIndex(
            model_name='album',
            index=models.Index(fields=['id'], name='music_album_id_a66d97_idx'),
        ),
        migrations.AddIndex(
            model_name='artist',
            index=models.Index(fields=['id'], name='music_artis_id_a6462a_idx'),
        ),
    ]