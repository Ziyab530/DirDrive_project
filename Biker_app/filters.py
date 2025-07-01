import django_filters
from .models import Biker, BikerAvailability, Earnings


class BikerFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(lookup_expr='icontains')
    cnic = django_filters.CharFilter(lookup_expr='iexact')
    joined_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Biker
        fields = ['full_name', 'cnic', 'bike_model', 'vehicle_number', 'joined_at']


class BikerAvailabilityFilter(django_filters.FilterSet):
    is_available = django_filters.BooleanFilter()
    updated_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = BikerAvailability
        fields = ['is_available', 'updated_at']


class EarningsFilter(django_filters.FilterSet):
    daily_earning = django_filters.RangeFilter()
    weekly_earning = django_filters.RangeFilter()
    monthly_earning = django_filters.RangeFilter()
    rating = django_filters.RangeFilter()

    class Meta:
        model = Earnings
        fields = ['daily_earning', 'weekly_earning', 'monthly_earning', 'rating']
