# Generated by Django 3.2.3 on 2021-06-15 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0016_show_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='post_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
