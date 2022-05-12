# Generated by Django 4.0.2 on 2022-05-06 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nft', '0004_rename_user_name_account_username_account_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('address', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
                ('confpass', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='Account',
        ),
    ]