from django.http import JsonResponse
from .models import Stock
from .serializers import StockSerializer

def stock_list(request):
    stocks = Stock.objects.all()
    serializer = StockSerializer(stocks, many=True)
    return JsonResponse({'stock':serializer.data})