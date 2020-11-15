from django.shortcuts import render
from .forms import ContactForm, ProductModelsForm
from django.contrib import messages
from .models import Product
from django.shortcuts import redirect

# Create your views here.
def index(request):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'index.html', context)

def contact(request):
    form = ContactForm(request.POST or None)

    if str(request.method)=='POST':
        if form.is_valid():
            form.send_mail()
            # nome=form.cleaned_data['nome']
            # email=form.cleaned_data['email']
            # assunto=form.cleaned_data['assunto']
            # mensagem=form.cleaned_data['mensagem']

            # print('Mensagem enviada')
            # print(f'Nome: {nome}')
            # print(f'E-mail: {email}')
            # print(f'Assunto: {assunto}')
            # print(f'Mensagem: {mensagem}')

            messages.success(request, 'Email enviado')
            form = ContactForm()

        else:
            messages.error(request,'Erro ao enviar')        

    context = {
        'form': form
    }
    return render(request, 'contact.html', context)

def product(request):
    if str(request.user) != 'AnonymousUser':
        if str(request.method) =='POST':
            form = ProductModelsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                # prod = form.save(commit=False)
                messages.success(request, 'Produto salvo')
                form = ProductModelsForm()
            else:
                messages.error(request,'Não foi salvo')
                form = ProductModelsForm()
        else:
            form = ProductModelsForm()
        context = {
            'form': form
        }
        return render(request, 'product.html', context)
    else:
        return redirect('index.html')
    