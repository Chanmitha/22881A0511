
from django.urls import path
from . import views

urlpatterns = [
    path('shorturls', views.create_short_url),
    path('shorturls/<str:shortcode>', views.get_short_url_stats),
]