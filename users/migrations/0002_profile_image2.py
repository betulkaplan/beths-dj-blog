# Generated by Django 3.2.5 on 2021-07-29 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image2',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics2'),
        ),
    ]