# Generated by Django 3.1.5 on 2021-01-07 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_editor_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_image',
            field=models.ImageField(blank=True, default='DEFAULT VALUE', null=True, upload_to='articles/'),
        ),
    ]
