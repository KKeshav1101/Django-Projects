# Generated by Django 5.1.1 on 2024-10-18 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_name', models.CharField(max_length=30)),
                ('S_regno', models.IntegerField()),
                ('S_M1', models.FloatField()),
                ('S_M2', models.FloatField()),
            ],
        ),
    ]
