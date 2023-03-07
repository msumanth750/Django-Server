from prices.models import Price
from stock.models import Stock
from receits.models import Receit

def get_price(brand,date):
    price =Price.objects.order_by('-effective_date').filter(brand=brand,effective_date__lte=date).first()
    if price:
        return price

def get_ostock(brand,date):
    stock = Stock.objects.filter(brand=brand,date=date).order_by('-date').first()
    if stock:
        return stock
    else:
        return None
def get_receit(brand,date):
    receit = Receit.objects.filter(brand=brand,date=date).order_by('-date').first()
    if receit:
        return receit
    else:
        return None
