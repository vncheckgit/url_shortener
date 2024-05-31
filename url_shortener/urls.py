from django.contrib import admin
from django.urls import path
from shortener import views
from shortener.views import redirect_to_admin

urlpatterns = [
    path('admin', admin.site.urls),
    path('<str:short_code>/', views.redirect_url, name='redirect_url'),
    path('', admin.site.urls),
]
