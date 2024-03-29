# Generated by Django 3.2.15 on 2023-03-16 02:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20230316_0933'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorsWife',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='姓名')),
                ('age', models.IntegerField(verbose_name='年龄')),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.author')),
            ],
            options={
                'verbose_name': '作者的妻子',
                'verbose_name_plural': '作者的妻子',
                'db_table': 'authorsWife',
            },
        ),
    ]
