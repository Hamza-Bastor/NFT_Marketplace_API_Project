# Generated by Django 4.0.2 on 2022-05-23 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nft', '0010_rename_email_account_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='password1',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='account',
            name='password2',
        ),
    ]
