import requests
import base64

def connect_to_dmh_api():
    # Sua chave de API DMH
    api_key_user = "204341de-b52b-45bd-a176-a5203335a01d"
    api_key_secret = "oL28Q~lAGUpcbN1CLHPkSfAE0.dWmt.FBv452c6m"
    api_key = "VmxRWGo0a0JTZFE2VW9QcHNCTVQ6T3BxX0kxaGhSZXl6aXhxZFF1c3BTQQ"

    # Combine a chave de API user e secret separados por dois pontos
    api_key_combined = f"{api_key_user}:{api_key_secret}"

    # Codificar a chave de API em base64
    api_key_base64 = base64.b64encode(api_key_combined.encode()).decode()

    # URL da API DMH para buscar os cursos
    url_busca_cursos = "https://elk-backbone-us-prd.es.eastus.azure.elastic-cloud.com:9243/financial-business-offer/_search"

    # Parâmetros da busca
    parametros_busca = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"accountTeachingInstitution.address.mailingCity": "cidade"}},
                    {"match": {"accountTeachingInstitution.address.mailingState": "estado"}}
                ]
            }
        }
    }

    # Cabeçalho de autorização para enviar na solicitação
    headers = {
        "GET": url_busca_cursos,
        "Content-Type": "application/json",
        "Authorization": f"Basic {api_key_base64}"
    }

    # Fazendo a solicitação GET com os parâmetros da busca e cabeçalhos de autorização
    response = requests.get(url_busca_cursos, json=parametros_busca, headers=headers)

    # Verificando se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Convertendo a resposta para JSON
        dados_resposta = response.json()
        print("Conexão bem-sucedida!")
        return dados_resposta
    else:
        print("Erro na conexão:", response.status_code)
        return {'error': 'Erro na solicitação para buscar cursos'}

if __name__ == "__main__":
    connect_to_dmh_api()
