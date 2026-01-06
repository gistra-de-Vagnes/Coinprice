from django.shortcuts import render
from .models import Coin
import json

def home(request):
    coins = Coin.objects.all()
    coin_data = {
        coin.symbol: {
            'name': coin.name,
            'symbol': coin.symbol.replace('USDT', ''),
            'icon': coin.icon
        }
        for coin in coins
    }

    context = {
        'coins_json': json.dumps(coin_data)
    }

    return render(request, 'prices/home.html', context)
