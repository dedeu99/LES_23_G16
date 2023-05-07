from django import forms
from django.forms import ModelForm
from .models import Pedido, PedidoHorario, Estado, UC, PedidoUC, Outros, AnoLetivo
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

class UCForm(forms.ModelForm):
    class Meta:
        model = UC
        exclude = ['pedido_uc']

class PedidoUCForm(forms.Form):
    pedido_uc = PedidoForm()
    uc = UCForm()

    def clean(self):
        cleaned_data = super().clean()
        pedido_uc = cleaned_data.get('pedido_uc')
        uc = cleaned_data.get('uc')

        if not pedido_uc.is_valid() or not uc.is_valid():
            raise forms.ValidationError('Os dados do pedido e da UC são inválidos.')

        return cleaned_data

    def save(self):
        pedido_uc = self.cleaned_data['pedido_uc'].save()
        uc = self.cleaned_data['uc'].save(commit=False)
        uc.pedido_uc = pedido_uc
        uc.save()
        return uc
    

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

    

class EmailForm(forms.Form):
    remetente = forms.CharField(max_length=150)
    senha = forms.CharField(max_length=150, widget=forms.PasswordInput)
    assunto = forms.CharField(max_length=100)
    descricao = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["assunto"].widget.attrs.update({"class": "form-control", "placeholder": "Assunto"})
        self.fields["descricao"].widget.attrs.update({"class": "form-control", "placeholder": "Descrição"})
        self.fields["remetente"].widget.attrs.update({"class": "form-control", "placeholder": "Remetente"})
        self.fields["senha"].widget.attrs.update({"class": "form-control", "placeholder": "Senha"})


class ConfirmacaoForm(forms.Form):
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)

class AnoLetivoForm(forms.ModelForm):
    class Meta:
        model = AnoLetivo
        fields = ['nome', 'data_inicial', 'data_final']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'data_inicial': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'data_final': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }