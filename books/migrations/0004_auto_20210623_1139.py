# Generated by Django 3.2.4 on 2021-06-23 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20210622_1535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['title']},
        ),
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(max_length=75, null=True),
        ),
    ]
