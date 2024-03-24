from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return render(request, 'index.html')

def receber_dados(nome, email, mensagem):
    # imprime os dados
    print("Nome:", nome)
    print("Email:", email)
    print("Mensagem:", mensagem)

def ler(request):

    if request.method == 'POST':
        # Obtém os dados do formulário
        nome = request.POST.get('nome', '')
        email = request.POST.get('email', '')
        mensagem = request.POST.get('mensagem', '')

        # Chama a função para processar os dados
        receber_dados(nome, email, mensagem)

        return render(request, 'pessoa.html', {'nome': nome, 'email': email, 'mensagem': mensagem})
    else:
        return HttpResponse('Método não permitido.', status=405)






