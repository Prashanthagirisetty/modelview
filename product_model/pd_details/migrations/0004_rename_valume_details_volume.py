# Generated by Django 4.0 on 2022-01-04 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pd_details', '0003_alter_details_costperitem_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='details',
            old_name='valume',
            new_name='volume',
        ),
    ]
