# Generated by Django 5.1.3 on 2024-11-10 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('fid', models.IntegerField()),
                ('dept', models.CharField(max_length=10)),
                ('fields', models.CharField(max_length=20)),
            ],
        ),
    ]