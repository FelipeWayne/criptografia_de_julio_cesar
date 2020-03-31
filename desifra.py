import json
import hashlib
import requests
from credenciais import token

abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
abc2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


URL = 'https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token=' + token
r = requests.get(URL)

if r.status_code == 200:
    print('Success!')

    with open('answer.JSON', 'w') as outfile:
        json.dump(r.json(), outfile)

elif r.status_code == 404:
    print('Not Found.')
    exit()
else:
    print('Error')
    exit()


cifrado = r.json()['cifrado']
numero_casas = r.json()['numero_casas']


decifrado = ''

for letra_ci in cifrado:
    if letra_ci not in abc:
        decifrado = decifrado + letra_ci
    else:
        conta = -1
        for letra in abc:
            conta += 1
            if letra == letra_ci:
                decifrado = decifrado + str(abc2[conta - numero_casas])


print("Decifrado: ", decifrado)
r.json()['decifrado'] = decifrado

resumo = hashlib.sha1()

decifrado = decifrado.encode('utf-8')

resumo.update(b''+ decifrado)

r.json()['resumo_criptografico'] = resumo.hexdigest()


with open('answer.JSON', 'w') as outfile:
    json.dump(r.json(), outfile)