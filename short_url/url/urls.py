from django.urls import path
from url.views import UrlView, redirect_url


urlpatterns = [
    path('', UrlView.as_view(), name='form'),
    path('<slug:short_url>/', redirect_url, name='s_code'),
]
