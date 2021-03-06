# Generated by Django 4.0.2 on 2022-02-21 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bioguide_id', models.CharField(max_length=7)),
                ('office', models.CharField(max_length=500)),
                ('quarter', models.CharField(max_length=1)),
                ('program', models.CharField(max_length=500)),
                ('category', models.CharField(max_length=500)),
                ('sort_sequence', models.CharField(max_length=500)),
                ('date', models.DateField(blank=True, null=True)),
                ('transcode', models.CharField(max_length=15)),
                ('recordid', models.CharField(blank=True, max_length=500, null=True)),
                ('payee', models.CharField(max_length=500)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('purpose', models.CharField(max_length=500)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=20)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
