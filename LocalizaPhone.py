import phonenumbers

#ajuste do telefone para usarmos o phonenumbers
telefone = input('Digite o número de telefone que você deseja encontrar: ')
telefone_ajustado = phonenumbers.parse(telefone)
print(telefone_ajustado)

#descobrir a localização do telefone
from phonenumbers import geocoder

local = geocoder.description_for_number(telefone_ajustado, 'pt-br')
print(local)

#descobrir a operadora do telefone 
from phonenumbers import carrier 
operadora = carrier.name_for_number(telefone_ajustado, 'pt-br')
print(operadora)

#encontrar telefone em um texto

texto = input('Digite um texto com um ou mais números de telefone para encontrar: ')

for telefone in phonenumbers.PhoneNumberMatcher(texto, 'BR'):
    print(telefone)
