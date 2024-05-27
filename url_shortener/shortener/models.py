from django.contrib.sites.models import Site
from django.db import models
import string
import random
from django.contrib.auth.models import User


def generate_short_code(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


class URL(models.Model):
    original_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True, default=generate_short_code)
    shortened_link = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        current_site = Site.objects.get_current()
        domain = current_site.domain
        self.shortened_link = f"{domain}{self.short_code}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.short_code} -> {self.original_url}'


class QRCode(models.Model):
    url = models.OneToOneField(URL, on_delete=models.CASCADE, related_name='qr_code')
    image = models.ImageField(upload_to='qr_codes/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'QR Code for {self.url.short_code}'
