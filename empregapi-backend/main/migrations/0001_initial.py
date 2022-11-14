# Generated by Django 4.0.4 on 2022-11-14 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=20)),
                ('address', models.TextField()),
            ],
        ),
    ]
