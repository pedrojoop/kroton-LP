import base64

def encode_api_keys(api_key_user, api_key_secret):
    # Combine a chave de API user e secret separados por dois pontos
    api_key_combined = f"{api_key_user}:{api_key_secret}"

    # Codificar a chave de API em base64
    api_key_base64 = base64.b64encode(api_key_combined.encode()).decode()

    return api_key_base64

if __name__ == "__main__":
    # Defina suas chaves de API
    api_key_user = "204341de-b52b-45bd-a176-a5203335a01d"
    api_key_secret = "oL28Q~lAGUpcbN1CLHPkSfAE0.dWmt.FBv452c6m"

    # Codificar as chaves
    encoded_key = encode_api_keys(api_key_user, api_key_secret)

    # Imprimir a chave codificada
    print("Chave codificada em base64:", encoded_key)
