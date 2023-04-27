from django import forms
from django.forms import ModelForm
from .models import Pedido, PedidoHorario, Estado, PedidoUC, Outros, PedidoSala
from django.forms.fields import DateField
from django.core.exceptions import ValidationError
from datetime import date, timedelta
from django.forms import ModelForm, ValidationError
from django import forms
from .models import Pedido, Estado
from datetime import date, timedelta


def validate_data_alvo(value):
    today = date.today()
    max_date = today + timedelta(days=1*365)
    if value < today:
        raise ValidationError("A data selecionada não pode ser uma data passada.")
    if value > max_date:
        raise ValidationError("A data selecionada não pode ser mais de 1 ano no futuro.")

class PedidoForm(ModelForm):
    estadoid = forms.ModelChoiceField(label='Estado', queryset=Estado.objects.all(), required=False, widget=forms.Select(attrs={'class': '', 'disabled': ''}))
    dataAlvo = forms.DateField(label='Data Alvo', widget=forms.DateInput(attrs={'class': 'input', 'type': 'date'}), validators=[validate_data_alvo])

    class Meta:
        model = Pedido
        fields = '__all__'
        exclude = ['id', 'funcionariopessoaid', 'docentepessoaid', 'datevalidation', 'datecreation']
        widgets = {
            'assunto': forms.TextInput(attrs={'class': 'input'}),
            'descricao': forms.Textarea(attrs={'class': 'textarea'}),
            'dataAlvo': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),
        }

class PedidoHorarioForm(ModelForm):
    
    class Meta:
        model = PedidoHorario
        fields = '__all__'
        exclude = ['pedidoid','datanova','horarioid2','horarioid']
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

class PedidoOutroForm(ModelForm):
    
    class Meta:
        model = Outros
        fields = '__all__'
        exclude = ['pedidoid']
        widgets = {
            'tipoalteracaoid': forms.Select(attrs={'class':'input'}),
            'unidadec': forms.Select(attrs={'class':'input'}),
            'motivopedido': forms.TextInput(attrs={'class':'input'}),
            #'estadoid': forms.Select(attrs={'class':'input'}),
            #'dataAlvo':forms.SelectDateWidget(attrs={'class':'date'})
        }

class PedidoSalaForm(ModelForm):
    
    class Meta:
        model = PedidoSala
        fields = '__all__'
        exclude = ['pedidoid']
        widgets = {
            'motivopedido': forms.TextInput(attrs={'class':'input'}),
            'id_sala': forms.Select(attrs={'class':'input'}),
            'dataalterar': forms.DateInput(attrs={'class':'input','type':'date'}),
            'datanova': forms.DateInput(attrs={'class':'input','type':'date'}),
        }

class PedidoUCForm(ModelForm):
    class Meta:
        model = PedidoUC
        fields = '__all__'
        exclude = ['pedidoid', 'motivopedido', 'id_uc', 'dataalterar', 'datanova']
        widgets = {
            'motivopedido': forms.TextInput(attrs={'class':'input'}),
            'semestrelecionada': forms.Select(attrs={'class':'input'}),
            'dataalterar': forms.DateInput(attrs={'class':'input','type':'date'}),
            'datanova': forms.DateInput(attrs={'class':'input','type':'date'}),
            'nomeuc':forms.TextInput(attrs={'class':'input'}),
            'anolecionada':forms.Select(attrs={'class':'input'}),
            'horas_semanais':forms.TextInput(attrs={'class':'input'}),
            'horas_periodo':forms.TextInput(attrs={'class':'input'}),
            'data_inicio': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),  # Alterado para DateInput
            'data_fim': forms.DateInput(attrs={'class': 'input', 'type': 'date'}),  # Alterado para DateInput
            'regente':forms.TextInput(attrs={'class':'input'}),
            'curso':forms.TextInput(attrs={'class':'input'}),
        }