from django.http import JsonResponse
from .ibge_api import obter_lista_estados
import requests
import base64

def obter_estados(request):
    lista_estados = obter_lista_estados()
    if lista_estados:
        # Criar uma lista de dicionários contendo o nome e o ID de cada estado
        estados = [{'nome': estado['nome'], 'id': estado['id']} for estado in lista_estados]
        return JsonResponse(estados, safe=False)
    else:
        return JsonResponse({'error': 'Erro ao obter a lista de estados'}, status=500)

def obter_cidades(request):
    estado = request.GET.get('estado')  
    print("Estado recebido:", estado)  # Debug: Verifica se o estado está sendo recebido corretamente
    
    url = f"https://servicodados.ibge.gov.br/api/v1/localidades/estados/{estado}/municipios"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Dados da resposta:", data)  # Debug: Verifica os dados da resposta da API

        cidades_do_estado = [cidade['nome'] for cidade in data]
        print("Cidades do estado:", cidades_do_estado)  # Debug: Verifica as cidades extraídas da resposta

        return JsonResponse(cidades_do_estado, safe=False)
    else:
        print("Erro ao obter a lista de cidades. Código de status:", response.status_code)
        return JsonResponse([], safe=False)
    
def buscar_cursos(request):
    # Obter a cidade e o estado fornecidos pelo usuário
    cidade = request.GET.get('cidade__finder')
    estado = request.GET.get('estado__finder')

    # Sua chave de API DMH
    api_key_user = "204341de-b52b-45bd-a176-a5203335a01d"
    api_key_secret = "oL28Q~lAGUpcbN1CLHPkSfAE0.dWmt.FBv452c6m"

    # Combinação da chave de API user e secret separados por dois pontos
    api_key_combined = f"{api_key_user}:{api_key_secret}"

    # Codificar a chave de API em base64
    api_key_base64 = base64.b64encode(api_key_combined.encode()).decode()

    # Cabeçalhos para enviar na solicitação
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Basic {api_key_base64}"
    }

    # URL da API DMH para buscar os cursos
    url_busca_cursos = "https://elk-backbone-us-prd.es.eastus.azure.elastic-cloud.com:9243/financial-business-offer/_search"

    # Parâmetros da busca
    parametros_busca = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"accountTeachingInstitution.address.mailingCity": cidade}},
                    {"match": {"accountTeachingInstitution.address.mailingState": estado}}
                ]
            }
        }
    }

    # Fazendo a solicitação POST com os parâmetros da busca e cabeçalhos de autorização
    response = requests.post(url_busca_cursos, json=parametros_busca, headers=headers)

    # Verificando se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Convertendo a resposta para JSON
        dados_resposta = response.json()
        
        # Processar os dados da resposta conforme necessário
        # Por exemplo, extrair os cursos disponíveis
        cursos_disponiveis = dados_resposta.get("hits", {}).get("hits", [])
        
        # Retornar os cursos disponíveis como resposta
        return JsonResponse(cursos_disponiveis, safe=False)
    else:
        # Se houver algum erro na solicitação, retornar uma resposta de erro
        return JsonResponse({'error': 'Erro na solicitação para buscar cursos'}, status=response.status_code)