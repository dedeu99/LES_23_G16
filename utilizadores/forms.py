from django.forms import ModelForm
#from .models import Participante, ProfessorUniversitario, Utilizador, Coordenador, Colaborador, Administrador
from .models import Pessoa
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordChangeForm
from django.forms import *
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import PasswordResetForm

#from configuracao.models import Unidadeorganica, Departamento, Curso


class ParticipanteForm(UserCreationForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

class EmailValidationOnForgotPassword(PasswordResetForm):

    def clean_email(self):
        email = self.cleaned_data['email']
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise forms.ValidationError(f'Este email não é válido!')
        return email



#USER_CHOICES = (
#    ("Utilizador", "Todos os Utilizadores"),
#    ("Participante", "Participantes"),
#    ("ProfessorUniversitario", "Professores Universitarios"),
#    ("Coordenador", "Coordenadores"),
#    ("Colaborador", "Colaboradores"),
#)

ESTADOS = (
    ("", "Todos os Estados"),
    ("T", "Confirmado"),
    ("F", "Pendente"),
    ("R", "Rejeitado"),
)




#class UtilizadorFiltro(Form):
#    filtro_tipo = ChoiceField(
#        choices=USER_CHOICES,
#        widget=Select(),
#        required=False,
#    )

#    filtro_estado = ChoiceField(
#        choices=ESTADOS,
#        widget=Select(),
#        required=False,
#    )


class LoginForm(AuthenticationForm):
    username=CharField(widget=TextInput(attrs={'class':'input','style':''}), label="Nome de Utilizador", max_length=255, required=False)
    password=CharField(widget=PasswordInput(attrs={'class':'input','style':''}), label= 'Senha', max_length=255, required=False)


class RecuperarPasswordForm(Form):
    email=CharField(widget=EmailInput(attrs={'class':'input','style':''}), label="Email", max_length=255, required=False)


