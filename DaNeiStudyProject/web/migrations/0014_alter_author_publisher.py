# Generated by Django 3.2.15 on 2023-03-16 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0013_author_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='publisher',
            field=models.ManyToManyField(to='web.Publisher', verbose_name='出版社'),
        ),
    ]