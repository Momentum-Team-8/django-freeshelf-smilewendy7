# Generated by Django 3.2.4 on 2021-06-24 04:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20210623_2316'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='favorites',
        ),
        migrations.AddField(
            model_name='book',
            name='favorites',
            field=models.ManyToManyField(null=True, related_name='books', to=settings.AUTH_USER_MODEL),
        ),
    ]
