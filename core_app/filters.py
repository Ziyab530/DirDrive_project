import django_filters
from .models import Ride, RideRequest, Transaction, Rating, History,price_info


class RideFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(lookup_expr='iexact')
    payment_method = django_filters.CharFilter(lookup_expr='iexact')
    date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Ride
        fields = ['user', 'biker', 'status', 'payment_method', 'date']


class RideRequestFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = RideRequest
        fields = ['user', 'biker', 'status']


class TransactionFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(lookup_expr='iexact')
    payment_method = django_filters.CharFilter(lookup_expr='iexact')
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Transaction
        fields = ['ride', 'status', 'payment_method', 'created_at']


class RatingFilter(django_filters.FilterSet):
    rating = django_filters.RangeFilter()
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Rating
        fields = ['ride', 'user', 'biker', 'rating', 'created_at']


class HistoryFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(lookup_expr='iexact')
    date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = History
        fields = ['user', 'ride', 'status', 'date']
class price_infoFilter(django_filters.FilterSet):
     status = django_filters.CharFilter(lookup_expr='iexact')
     date = django_filters.DateFromToRangeFilter()
    
     class Meta :
         model = price_info
         fields = ['price_id','price']
         