import django_filters
from .models import Pedido
from django.db.models import Q

def filter_nome(queryset, name, value):
    for term in value.split():
        queryset = queryset.filter(Q(first_name__icontains=term)
                                   | Q(last_name__icontains=term))
    return queryset

def filter_ID(queryset, name, value):
    for term in value.split():
        queryset = queryset.filter(Q(id__icontains=term))
    return queryset

class PedidosFilter(django_filters.FilterSet):
    ID = django_filters.CharFilter(method=filter_ID)
    class Meta:
        model = Pedido
        fields = '__all__'