# Coinprice/asgi.py

import os
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.core.asgi import get_asgi_application
import prices.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Coinprice.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            prices.routing.websocket_urlpatterns
        )
    ),
})
