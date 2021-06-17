# Generated by Django 3.2.3 on 2021-06-05 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('radio', '0011_audio_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='favorite',
            field=models.ManyToManyField(related_name='audio_favorite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='audio',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='radio.show'),
        ),
    ]