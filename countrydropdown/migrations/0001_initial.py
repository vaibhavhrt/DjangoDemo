# Generated by Django 3.1.5 on 2021-03-17 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=127)),
                ('state', models.CharField(max_length=127)),
                ('country', models.CharField(max_length=127)),
            ],
        ),
        migrations.CreateModel(
            name='CountrySelect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=127)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='countrydropdown.location')),
            ],
        ),
    ]
