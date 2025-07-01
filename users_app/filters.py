import django_filters
from .models import UserProfile, BikerApplication, SupportIssue

class UserProfileFilter(django_filters.FilterSet):
    gender = django_filters.CharFilter(lookup_expr='iexact')
    date_of_birth = django_filters.DateFilter()
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = UserProfile
        fields = ['gender', 'date_of_birth', 'created_at']


class BikerApplicationFilter(django_filters.FilterSet):
    status = django_filters.CharFilter(lookup_expr='iexact')
    submitted_at = django_filters.DateFromToRangeFilter()
    reviewed_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = BikerApplication
        fields = ['status', 'submitted_at', 'reviewed_at', 'bikeModel']


class SupportIssueFilter(django_filters.FilterSet):
    issue_type = django_filters.CharFilter(lookup_expr='iexact')
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = SupportIssue
        fields = ['issue_type', 'created_at']
