# Generated by Django 3.1.3 on 2020-11-20 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Contact', '0003_accounts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Accounts',
            new_name='Account',
        ),
    ]