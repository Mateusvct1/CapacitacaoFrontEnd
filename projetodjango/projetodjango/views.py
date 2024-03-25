from django.http import HttpResponse
from django.shortcuts import render
#HttpResponse é usado para retornar respostas HTTP
#render é usado para renderizar templates.

# Define uma função que aceita um objeto de requisição Django
def hello(request):
# Renderiza o template 'index.html' e o retorna como resposta    
    return render(request, 'index.html')
# Define uma função que aceita três argumentos
def receber_dados(nome, email, mensagem):
    # imprime os dados
    print("Nome:", nome)
    print("Email:", email)
    print("Mensagem:", mensagem)
# Define uma função que aceita um objeto de requisição Django
def ler(request):
# Verifica se o método da requisição é POST
#O método POST é um método de requisição HTTP utilizados para enviar dados para o servidor.    
    if request.method == 'POST':
        # Obtém os dados do formulário
        nome = request.POST.get('nome', '')
        email = request.POST.get('email', '')
        mensagem = request.POST.get('mensagem', '')

        # Chama a função para processar os dados
        receber_dados(nome, email, mensagem)
# Retorna uma resposta renderizando o template 'pessoa.html' com os dados do formulário como contexto
        return render(request, 'pessoa.html', {'nome': nome, 'email': email, 'mensagem': mensagem})
    else:
        return HttpResponse('Método não permitido.', status=405)
