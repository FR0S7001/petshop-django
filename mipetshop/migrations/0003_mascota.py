# Generated by Django 5.0.6 on 2024-07-19 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mipetshop', '0002_cliente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('especie', models.CharField(max_length=100)),
                ('raza', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
    ]
