# Generated by Django 5.0.6 on 2024-11-18 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserServices', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='profile_pic',
            field=models.TextField(),
        ),
    ]
