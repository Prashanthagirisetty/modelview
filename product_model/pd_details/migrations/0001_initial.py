# Generated by Django 4.0 on 2022-01-04 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=30)),
                ('costperitem', models.DecimalField(decimal_places=30, max_digits=30)),
            ],
        ),
    ]
