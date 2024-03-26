import requests
import requests
from django.http import JsonResponse

def obter_lista_estados():
    # Endpoint da API do IBGE para obter a lista de estados
    url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/"

    # Fazendo a solicitação GET
    response = requests.get(url)

    # Verificando se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Convertendo a resposta para JSON
        data = response.json()

        # Retornar a lista de estados
        return data
    else:
        # Se a solicitação não foi bem-sucedida, exibir uma mensagem de erro
        print("Erro ao obter a lista de estados. Código de status:", response.status_code)
        return None
# Chamando a função para obter a lista de estados
lista_estados = obter_lista_estados()



def obter_cidades(request):
    estado = request.GET.get('estado')  # Obtém o estado da solicitação GET
    
    # Endpoint da API do IBGE para obter a lista de cidades de um estado específico
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado}/municipios"

    # Fazendo a solicitação GET
    response = requests.get(url)

    # Verificando se a solicitação foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Convertendo a resposta para JSON
        data = response.json()

        # Extraindo apenas os nomes das cidades
        cidades_do_estado = [cidade['nome'] for cidade in data]

        return JsonResponse(cidades_do_estado, safe=False)
    else:
        # Se a solicitação não foi bem-sucedida, retornar uma lista vazia
        print("Erro ao obter a lista de cidades. Código de status:", response.status_code)
        return JsonResponse([], safe=False)