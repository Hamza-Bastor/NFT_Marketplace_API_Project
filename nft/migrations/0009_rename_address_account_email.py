# Generated by Django 4.0.2 on 2022-05-22 21:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nft', '0008_rename_password_account_password1_account_password2'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='address',
            new_name='email',
        ),
    ]
