# Generated by Django 4.2.4 on 2023-08-03 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(default='default.png', upload_to='media/default_book_covers/'),
        ),
    ]
