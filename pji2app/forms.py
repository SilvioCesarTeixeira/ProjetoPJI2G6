from django.forms import ModelForm
from pji2app.models import Cadastro


class CadastroForm(ModelForm):
    class Meta:
        model = Cadastro
        fields = ['inputEmpresa', 'inputCNPJ', 'inputEmail', 'inputTel', 'inputCel', 'inputAddress', 'inputNumber', 'inputAddress2', 'inputCEP', 'inputCity', 'inputEstado','inputTipo']
        #inputTipo define qual lado da cadeia de produção está a empresa: 'True' para produtor, 'False' para reciclador
