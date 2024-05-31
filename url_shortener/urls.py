from django.contrib import admin
from django.urls import path
from shortener import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('<str:short_code>/', views.redirect_url, name='redirect_url'),
    path('', admin.site.urls),
]
