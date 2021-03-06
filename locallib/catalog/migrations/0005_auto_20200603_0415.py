# Generated by Django 3.0.4 on 2020-06-03 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200603_0413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='genre',
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Select a genre for this book', to='catalog.Genre'),
        ),
    ]
