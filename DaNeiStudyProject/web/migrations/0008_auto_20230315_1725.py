# Generated by Django 3.2.15 on 2023-03-15 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_alter_author_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['publicate_date'], 'verbose_name': '书籍', 'verbose_name_plural': '书籍'},
        ),
        migrations.AlterModelTable(
            name='book',
            table='book',
        ),
    ]
