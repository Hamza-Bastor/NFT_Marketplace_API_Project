# Generated by Django 4.0.2 on 2022-05-24 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nft', '0012_remove_collection_collection_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
