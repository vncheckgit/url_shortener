from django.shortcuts import redirect, get_object_or_404
from .models import URL


def redirect_url(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    url.click_count += 1
    url.save()
    return redirect(url.original_url)

