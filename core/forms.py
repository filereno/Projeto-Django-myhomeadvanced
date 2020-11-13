from django import forms
from django.core.mail.message import EmailMessage
from .models import Product

class ContactForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=150)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea(), max_length=1000)

    def send_mail(self):
        nome=self.cleaned_data['nome']
        email=self.cleaned_data['email']
        assunto=self.cleaned_data['assunto']
        mensagem=self.cleaned_data['mensagem']

        cont_email = f'Nome: {nome}\nE-mail: {email}\nAssunnto: {assunto}\nMenssagem: {mensagem}'

        mail = EmailMessage(
            subject='Email enviado pelo site',
            body=cont_email,
            from_email='contato@seudominio.com.br',
            to=['contato@seudominio.com.br',],
            headers={'Reply-To': email}
        )
        mail.send()

class ProductModelsForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = ['nome', 'preco', 'estoque', 'imagem']