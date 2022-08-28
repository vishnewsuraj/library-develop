# Generated by Django 4.0.3 on 2022-08-28 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=250)),
                ('pages', models.CharField(max_length=500)),
                ('isActive', models.CharField(max_length=50)),
            ],
        ),
    ]
