from django.contrib import admin
from django.urls import path, include
from shortener import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('<str:short_code>/', views.redirect_url, name='redirect_url'),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', admin.site.urls),
]
