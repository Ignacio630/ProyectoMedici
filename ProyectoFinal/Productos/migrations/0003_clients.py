# Generated by Django 4.1.5 on 2023-01-12 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Productos', '0002_providers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
