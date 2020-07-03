from .models import Branches
from .serializers import BranchSerializer
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters
from django_filters import FilterSet
from django_filters.rest_framework import DjangoFilterBackend


class BranchFilter(FilterSet):
    bank = filters.CharFilter('bank__Name')
    city = filters.CharFilter('city')
    ifsc = filters.CharFilter('ifsc')

    class Meta:
        model = Branches
        fields = ['bank', 'city', 'ifsc']


class BranchesList(ListAPIView):
    queryset = Branches.objects.all()
    serializer_class = BranchSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_class = BranchFilter


