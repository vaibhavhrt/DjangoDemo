# Generated by Django 3.1.7 on 2021-05-20 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bulkupdate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='staus',
        ),
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.PositiveIntegerField(choices=[(0, 'pending'), (1, 'completed')], default=0),
            preserve_default=False,
        ),
    ]
