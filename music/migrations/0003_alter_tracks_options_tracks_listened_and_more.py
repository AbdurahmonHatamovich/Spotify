# Generated by Django 5.0.4 on 2024-05-14 14:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_alter_album_artist_alter_album_cover_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tracks',
            options={'ordering': ('id',)},
        ),
        migrations.AddField(
            model_name='tracks',
            name='listened',
            field=models.PositiveBigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='album',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='music.artist'),
        ),
        migrations.AlterField(
            model_name='album',
            name='cover',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='image',
            field=models.URLField(null=True),
        ),
        migrations.AddIndex(
            model_name='tracks',
            index=models.Index(fields=['id'], name='music_track_id_310b0e_idx'),
        ),
    ]
