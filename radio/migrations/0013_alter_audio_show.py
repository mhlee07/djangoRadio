# Generated by Django 3.2.3 on 2021-06-05 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0012_auto_20210605_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio',
            name='show',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='audios', to='radio.show'),
        ),
    ]