# Generated by Django 4.1.4 on 2022-12-28 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='volunteers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('registration', models.CharField(max_length=15)),
                ('Mobile', models.CharField(max_length=12)),
                ('Email', models.CharField(max_length=50)),
                ('committee', models.CharField(max_length=50)),
                ('skills', models.CharField(max_length=300)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='registration',
        ),
    ]
