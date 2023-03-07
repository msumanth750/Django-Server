from rest_framework import serializers

from .models import Brand
from prices.models import Price
from stock.models import Stock
from receits.models import Receit
from django.db.models import Sum,Q

class BrandSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()
    sale = serializers.SerializerMethodField()
    stock = serializers.SerializerMethodField()
    class Meta:
        model = Brand
        fields = '__all__'

    def get_price(self,obj):
        request = self.context['request']
        start=request.query_params.get('sdate',None)
        end=request.query_params.get('edate',None)
        print(start,end)
        prices = Price.objects.filter(brand=obj,effective_date__lte=end)
        if prices:
            price = prices.order_by('-effective_date').first()
            return {'mrp':price.mrp,
                    'bp':price.bar_price,
                    'mp':price.min_price}
        else:
            return 0
    def get_sale(self,obj):
        return None
    def get_stock(self,obj):
        request = self.context['request']
        start=request.query_params.get('sdate',None)
        end=request.query_params.get('edate',None)
        if start and end:
            print('**************')
            stocks= Stock.objects.filter(brand=obj,date__gte=start,date__lte=end).aggregate(sum=Sum('quantity'))
            receits =Receit.objects.filter(brand=obj,date__gte=start,date__lte=end).aggregate(sum=Sum('quantity'))

            return int(stocks['sum'])+int(receits['sum']) if receits['sum'] else stocks['sum']
        else:
            return 0
