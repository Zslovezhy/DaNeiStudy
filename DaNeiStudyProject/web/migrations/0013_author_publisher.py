# Generated by Django 3.2.15 on 2023-03-16 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_book_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='publisher',
            field=models.ManyToManyField(to='web.Publisher'),
        ),
    ]
