import django_filters
from .models import Pedido,Docente,Funcionario
from django.db.models import Model


def filter_row(queryset, row, value):
    queryset = queryset.filter(funcionariopessoaid=value)
    return queryset

def filter_ID(queryset, name, value):
    for term in value.split():
        queryset = queryset.filter(Q(id__icontains=term))
    return queryset

class PedidosFilter(django_filters.FilterSet):
    ID = django_filters.CharFilter(method=filter_ID)
    #funcionario = django_filters.CharFilter(method=filter_row)
    class Meta:
        model = Pedido
        fields = '__all__'

    @property
    def qs(self):
        parent = super().qs

        #Se for Docente retorna só os seus pedidos
        if self.request.user is not None :
            if Docente.objects.filter(pessoaid=self.request.user.id).exists():
                return parent.filter(docentepessoaid=self.request.user.id)
            #Se for Funcionário retorna todos os pedidos
            if Funcionario.objects.filter(pessoaid=self.request.user.id).exists():
                return parent

        #não retorna pedidos -> não achei maneira mais bonita de fazer isto
        return parent.filter(id=-1)