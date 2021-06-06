# Generated by Django 3.1.7 on 2021-05-20 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sortnpage', '0004_paginationdemo_createdat'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateRangeAndDuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('duration_days', models.PositiveIntegerField()),
            ],
        ),
    ]