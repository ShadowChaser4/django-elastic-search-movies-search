# Generated by Django 4.1.4 on 2023-01-13 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_alter_actor_middle_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Actor',
            new_name='Artist',
        ),
    ]
