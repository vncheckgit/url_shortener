# Generated by Django 5.0.6 on 2024-05-27 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_url_user_qrcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='shortened_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
