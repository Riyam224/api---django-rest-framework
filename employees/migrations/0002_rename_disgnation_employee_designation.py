# Generated by Django 5.1.6 on 2025-02-10 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='disgnation',
            new_name='designation',
        ),
    ]
