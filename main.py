import requests

def main() :
    """Exibe dados de um CEP com base no input de seu respectivo número"""
	
    buscar_cep = input("Informe o CEP.\nExemplo: 31200123\n")

    url = f'http://www.viacep.com.br/ws/{buscar_cep}/json/'

    resposta = requests.get(url)
    print(resposta.status_code)

    if resposta.status_code == 200:
        
        resposta_json = resposta.json()
        print(resposta_json)

        if len(buscar_cep) == 8 and 'erro' not in resposta_json:
            
            bairro = resposta_json['bairro']
            logradouro = resposta_json['logradouro']
            localidade = resposta_json['localidade']
            uf = resposta_json['uf']

            print(bairro)
            print(logradouro)
            print(localidade)
            print(uf)
        
        else:
            print('Esse número de CEP não existe.')
    else:
        print('CEP informado é inválido. Tente novamente.')
        exit()

if __name__ == '__main__':
	main()
