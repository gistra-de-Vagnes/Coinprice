import json
import asyncio
import websockets
from channels.generic.websocket import AsyncWebsocketConsumer

class PriceConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.keep_running = True
        self.prices = {
            'BTCUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'ETHUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'BNBUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'SOLUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'DOGEUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'ADAUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'XRPUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'DOTUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'LTCUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'LINKUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'XLMUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'BCHUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'ALGOUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'VETUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'ICPUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'MATICUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'FILUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'TRXUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'ETCUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'ATOMUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'AVAXUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'XMRUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'EOSUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'NEOUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'XTZUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'AAVEUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'MKRUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'COMPUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'UNIUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'YFIUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'SHIBUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'INJUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'RUNEUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'GRTUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'CRVUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'SANDUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'MANAUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'ENJUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'AXSUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'CHZUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'FLOWUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'FTMUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'GALAUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'APEUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'THETAUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'ZILUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'HBARUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'ARPAUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'KAVAUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'ONEUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'ROSEUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'ANKRUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'SXPUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'LRCUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'ZECUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'},
            'DASHUSDT': {'price': 'N/A', 'high': 'N/A', 'low': 'N/A', 'volume': 'N/A'}
        }
        asyncio.create_task(self.binance_loop())

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
                    s = data.get('data', {}).get('s')
                    c = data.get('data', {}).get('c')
                    h = data.get('data', {}).get('h')
                    l = data.get('data', {}).get('l')
                    v = data.get('data', {}).get('v')
                    if s in self.prices:
                        self.prices[s] = {
                            'price': c,
                            'high': h,
                            'low': l,
                            'volume': v
                        }
                    await self.send(text_data=json.dumps(self.prices))
        except Exception as e:
            print("Lỗi Binance WS:", e)
            await self.send(text_data=json.dumps(self.prices))