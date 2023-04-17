from django import forms
from django.forms import ModelForm
from .models import Pedido, PedidoHorario, Estado, Uc, PedidoUc
from django.forms.fields import DateField

class PedidoForm(ModelForm):
    estadoid = forms.ModelChoiceField(label='Estado',queryset=Estado.objects.all(), required=False,widget=forms.Select(attrs={'class':'','disabled':''}))
    class Meta:
        model = Pedido
        fields = '__all__'
        exclude = ['id','funcionariopessoaid','docentepessoaid','datevalidation','datecreation']
        widgets = {
            'assunto': forms.TextInput(attrs={'class':'input'}),
            'descricao': forms.Textarea(attrs={'class':'textarea'}),
            'dataAlvo': forms.DateInput(attrs={'class':'input','type':'date'}),
            #'estadoid': forms.Select(attrs={'disabled':''}),
            #'dataAlvo':forms.SelectDateWidget(attrs={'class':'date'})
        }


class PedidoHorarioForm(ModelForm):
    
    class Meta:
        model = PedidoHorario
        fields = '__all__'
        exclude = ['pedidoid','dataalterar','datanova','horarioid2','horarioid']
        widgets = {
            'tipoalteracaoid': forms.Select(attrs={'class':'input'}),
            'unidadec': forms.Select(attrs={'class':'input'}),
            'motivopedido': forms.TextInput(attrs={'class':'input'}),
            #'estadoid': forms.Select(attrs={'class':'input'}),
            #'dataAlvo':forms.SelectDateWidget(attrs={'class':'date'})
        }

#class PedidoUcForm(ModelForm):
 #   class Meta:
  #      model = PedidoUc
   #     exclude = ['id']

class UcForm(ModelForm):
    class Meta:
        model = Uc
        fields = '__all__'
        exclude = ['id']
        widgets = {
            'tipoalteracaoid': forms.Select(attrs={'class':'input'}),
            'unidadec': forms.Select(attrs={'class':'input'}),
            'motivopedido': forms.TextInput(attrs={'class':'input'}),
            #'semestrelecionada': forms.NumberInput(attrs={'class': 'input'}),
            #'codigo_disciplina': forms.NumberInput(attrs={'class': 'input'}),
            #'nomeuc': forms.TextInput(attrs={'class': 'input'}),
            #'inst_disciplina': forms.TextInput(attrs={'class': 'input'}),
            #'turma': forms.TextInput(attrs={'class': 'input'}),
            #'anolecionada': forms.NumberInput(attrs={'class': 'input'}),
            #'horas_semanais': forms.TextInput(attrs={'class': 'input'}),
            #'horas_periodo': forms.TextInput(attrs={'class': 'input'}),
            #'data_inicio': forms.TextInput(attrs={'class': 'input'}),
            #'data_fim': forms.TextInput(attrs={'class': 'input'}),
        }