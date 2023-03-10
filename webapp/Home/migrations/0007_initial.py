# Generated by Django 4.1.4 on 2022-12-28 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Home', '0006_delete_volunteers'),
    ]

    operations = [
        migrations.CreateModel(
            name='volunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('regno', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('committee', models.CharField(max_length=100)),
                ('skills', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
    ]
