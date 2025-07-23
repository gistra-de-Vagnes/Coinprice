# Coinprice/price/routing.py

from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/price/$', consumers.PriceConsumer.as_asgi()),
]
