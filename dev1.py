import json
import random as rd
import math
from re import S

with open('dados.json', 'r') as f:
    dados_cru = f.read()

dicionario_continente = json.loads(dados_cru)


def normaliza(dicionario_continente):
    dicionário_paises = {}

    for continente in dicionario_continente:
        cont_pais = dicionario_continente[continente]
        for pais in cont_pais:
            dados = cont_pais[pais]
            dados['continente'] = continente

            dicionário_paises[pais] = dados 

    return dicionário_paises  
dicionário_paises = normaliza(dicionario_continente)    
i=0
lista_paises = []
def sorteia_pais (dicionario_paises):
    lista_paises = list(dicionario_paises.keys())
    pais_escolhido = rd.choice(lista_paises)
    return pais_escolhido

def haversine (r,laA,lonA,laB,lonB):
    latA =laA*math.pi/180
    longA = lonA*math.pi/180
    latB = laB*math.pi/180 
    longB = lonB*math.pi/180
    dif1=(latB-latA)/2
    dif2=(longB-longA)/2
    a= (math.sin(dif1))**2
    b= (math.sin(dif2))**2
    c=math.cos(latA)*math.cos(latB)
    angulo=math.sqrt(a+c*b)
    distancia=2*r*math.asin(angulo)
    return distancia 
    
def adiciona_em_ordem(pais,d,l):
    lista_d = []
    i=0
    while i <len(l):
        lista_d.append(l[i][1])
        i+=1
    print(lista_d)
    x = 0
    while x<len(lista_d):
        if d > lista_d[x]:
            x += 1
        elif d < lista_d[x]:
            break
    l.insert(x, [pais, d])
    return l  

def esta_na_lista (pais, lista_paises):
    i=0
    for e in lista_paises:
        if pais == e[0]:
            i+=1
            return True
    if i==0:
        return False
        
def cor_predominante(dicionario_continente):
    i = 0
    corp = ''
    for cor, valor in dicionario_continente.items():
        if dicionario_continente[cor] > i:
            i = dicionario_continente[cor]
            corp = cor
    return corp

def sorteia_letra(palavra,lista_restrita):
    letras_sorteio = []
    caracteres_especiais = ['.', ',', '-', ';', ' ']
    for letra in palavra:
        if letra not in lista_restrita and letra not in caracteres_especiais:
            letras_sorteio.append(letra)
    resultado = rd.choice(letras_sorteio)
    return resultado

def cor(r, g, b, texto):
    return f"\033[38;2;{r};{g};{b}m{texto}\033[38;2;255;255;255m"

###########################################################################################
ok = False
print(' ============================ ')
print('|                            |')
print('| Bem-vindo ao Insper Países |')
print('|                            |')
print(' ==== Design de Software ====') 
print(' Comandos:')
print('    dica       - entra no mercado de dicas')
print('    desisto    - desiste da rodada')
print('    inventario - exibe sua posição')
print(' Um país foi escolhido, tente adivinhar!')
print('PS:Escreva somente em letras minúsculas e sem acento!')
while ok == False:
    pronto = input('Pronto? (s/n)?')
    if pronto == 's':
        ok = True
        print('')
    if pronto == 'n':
        print('Ok, estamos te esperando... ;)')

pais_escolhido = sorteia_pais(dicionário_paises)
r = 6371

f = cor(36, 255, 160, '20')
m = cor(255, 248, 36, '10')
d = cor(255, 69, 36, '5')

facil = cor(36, 255, 160,'Fácil')
medio = cor(255, 248, 36, 'Médio')
dificil = cor(255, 69, 36, 'Difícil')

um = cor(36, 255, 160,'1')
dois = cor(255, 248, 36, '2')
tres = cor(255, 69, 36, '3')

escolha_dificuldade = f'[{um}|{dois}|{tres}]'

tentativas = 0
print('Mas antes de começarmos escolha a dificuldade do seu jogo...')
dif = int(input(f'Escolha sua dificuldade:\n   1. {facil} --> {f} tentativas\n   2. {medio} --> {m} tentativas\n   3. {dificil} --> {d} tentativas\n    Dificuldade escolhida {escolha_dificuldade}: '))
if dif == 1:
  tentativas += 20
elif dif == 2:
  tentativas += 10
elif dif == 3:
  tentativas += 5

while dif != 1 and dif != 2 and dif != 3:
  dif = int(input(f'Opção inválida. Escolha uma das seguintes: {escolha_dificuldade}: '))
  if dif == 1:
    tentativas += 20
  elif dif == 2:
    tentativas += 10
  elif dif == 3:
    tentativas += 5


area = (dicionário_paises[pais_escolhido])['area']
populacao = (dicionário_paises[pais_escolhido])['populacao']
capital = (dicionário_paises[pais_escolhido])['capital']
latitude = ((dicionário_paises[pais_escolhido])['geo'])['latitude']
longitude = ((dicionário_paises[pais_escolhido])['geo'])['longitude']
bandeira = (dicionário_paises[pais_escolhido])['bandeira']
continente = (dicionário_paises[pais_escolhido])['continente']
#########################

#########################

tentativas_u = 0
numero_tentativas = tentativas - tentativas_u
acerto = False
lista_jogadas = []
if tentativas > 10:
  print(f'Tentativas restantes:', f'\033[0;32m {tentativas}\033[0;0m')
elif tentativas <= 10 and tentativas > 5:
  print(f'Tentativas restantes:', f'\033[0;33m {tentativas}\033[0;0m')
elif tentativas <= 5:
  print(f'Tentativas restantes:', f'\033[0;31m {tentativas}\033[0;0m')

while tentativas_u < tentativas and acerto == False:
    pais = input(f'Você tem {numero_tentativas} tentativa(s)\nQual seu palpite?')
    if pais != pais_escolhido and pais != "dica" and pais != "inventario" and pais != "desisto" and pais in dicionário_paises and pais not in lista_jogadas:
        print('Errado!') 
        tentativas_u += 1
        numero_tentativas = tentativas - tentativas_u

    if pais in lista_jogadas and pais in dicionário_paises:
        print(f'Você já chutou {pais}! Tente com outro...')

    lista_jogadas.append(pais)

    if pais not in dicionário_paises and pais != (1,2,3,4,5,6) and pais != 'dica' and pais != 'inventario' and pais != 'desisto':
        print('País inválido.')


