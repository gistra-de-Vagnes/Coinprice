import json
import asyncio
import websockets
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import Coin

class PriceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.keep_running = True
        self.prices = await self.get_initial_prices()
        asyncio.create_task(self.binance_loop())

    @database_sync_to_async
    def get_initial_prices(self):
        coins = Coin.objects.all()
        return {
            coin.symbol: {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'}
            for coin in coins
        }

    async def disconnect(self, close_code):
        self.keep_running = False

    async def binance_loop(self):
        symbols = '/'.join([f"{s.lower()}@miniTicker" for s in self.prices.keys()])
        uri = f"wss://stream.binance.com:9443/stream?streams={symbols}"
        try:
            async with websockets.connect(uri) as ws:
                while self.keep_running:
                    msg = await ws.recv()
                    data = json.loads(msg)
                    stream_data = data.get('data', {})
                    symbol = stream_data.get('s')

                    if symbol in self.prices:
                        price_data = {
                            'price': stream_data.get('c'),
                            'high': stream_data.get('h'),
                            'low': stream_data.get('l'),
                            'volume': stream_data.get('v')
                        }

                        self.prices[symbol] = price_data

                        update_message = {
                            'symbol': symbol,
                            'data': price_data
                        }

                        await self.send(text_data=json.dumps(update_message))
        except Exception as e:
            print("Lỗi Binance WS:", e)