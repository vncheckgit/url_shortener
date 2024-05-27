from django.shortcuts import render, redirect, get_object_or_404
from .models import URL, QRCode
from .forms import URLForm
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    if request.method == 'POST':
        form = URLForm(request.POST)
        if form.is_valid():
            url = form.save(commit=False)
            url.user = request.user
            url.save()

            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(request.build_absolute_uri(f'/{url.short_code}'))
            qr.make(fit=True)

            img = qr.make_image(fill_color="black", back_color="white")
            buffer = BytesIO()
            img.save(buffer, format="PNG")

            # Save the QR code image
            qr_code = QRCode(url=url)
            filename = f'{url.short_code}.png'
            qr_code.image.save(filename, ContentFile(buffer.getvalue()), save=True)

            return render(request, 'shortener/success.html', {
                'url': url,
                'qr_code': qr_code
            })
    else:
        form = URLForm()
    return render(request, 'shortener/home.html', {'form': form})


def redirect_url(request, short_code):
    url = get_object_or_404(URL, short_code=short_code)
    url.click_count += 1
    url.save()
    return redirect(url.original_url)


def redirect_to_admin(request):
    return redirect('admin:index')