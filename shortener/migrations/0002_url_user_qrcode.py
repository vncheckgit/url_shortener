# Generated by Django 5.0.6 on 2024-05-27 04:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='QRCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='qr_codes/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('url', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='qr_code', to='shortener.url')),
            ],
        ),
    ]