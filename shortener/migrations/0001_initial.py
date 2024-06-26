# Generated by Django 3.2.22 on 2024-05-27 03:37

from django.db import migrations, models
import shortener.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('original_url', models.URLField()),
                ('short_code', models.CharField(default=shortener.models.generate_short_code, max_length=10, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('click_count', models.IntegerField(default=0)),
            ],
        ),
    ]
