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

tentativas_u = 0
numero_tentativas = tentativas - tentativas_u
acerto = False
lista_paiss = []
if tentativas > 10:
  print(f'Tentativas restantes:', f'\033[0;32m {tentativas}\033[0;0m')
elif tentativas <= 10 and tentativas > 5:
  print(f'Tentativas restantes:', f'\033[0;33m {tentativas}\033[0;0m')
elif tentativas <= 5:
  print(f'Tentativas restantes:', f'\033[0;31m {tentativas}\033[0;0m')

lista1= []
dicionario_distancia = {}
lista_distancia = []
cordica1 = cor(66, 135, 245,'4')
cordica2 = cor(66, 135, 245,'3')
cordica3 = cor(66, 135, 245,'6')
cordica4 = cor(66, 135, 245,'5')
cordica5 = cor(66, 135, 245,'7')
cordica6 = cor(66, 135, 245,'0')

dic_dicas = {
  1: f'1. Cor da bandeira  - custa {cordica1} tentativas.',
  2: f'2. Letra da capital - custa {cordica2} tentativas.',
  3: f'3. Área             - custa {cordica3} tentativas.',
  4: f'4. População        - custa {cordica4} tentativas.',
  5: f'5. Continente       - custa {cordica5} tentativas.',
  6: f'6. Sair do mercado.'
}

custo_dicas = {
        1: 4, 
        2: 3,
        3: 6,
        4: 5,
        5: 7,
        6: 0
              }

inventario = {}
dic_distancia = {}
cap= ''
lista_distancias = []
jogar_novamente = True 
lista_dist_colorido = []
lista_dicas = [1,2,3,4,5,6]
while tentativas_u < tentativas and acerto == False:
    pais = input(f'Você tem {numero_tentativas} tentativa(s)\nQual seu palpite?')
    if pais != pais_escolhido and pais != "dica" and pais != "inventario" and pais != "desisto" and pais in dicionário_paises and pais not in lista_paiss and pais != 'nardi':
        print('Errado!') 
        tentativas_u += 1
        numero_tentativas = tentativas - tentativas_u

    if pais in lista_paiss and pais in dicionário_paises:
        print(f'Você já chutou {pais}! Tente com outro...')

    lista_paiss.append(pais)

    if pais not in dicionário_paises and pais != (1,2,3,4,5,6) and pais != 'dica' and pais != 'inventario' and pais != 'desisto' and pais != 'nardi':
        print('País inválido.')

    if pais == 'nardi':
        print('Uau! Parabéns você achou o easter egg!')
        tentativas+=1000000000000000
        numero_tentativas = tentativas - tentativas_u
    if pais in dicionário_paises:
        distancia = haversine(r, ((dicionário_paises[pais])['geo'])['latitude'], ((dicionário_paises[pais])['geo'])['longitude'], latitude, longitude)
        if pais not in lista1:
            lista1.append(pais)
        dicionario_distancia[distancia] = pais
        for e in dicionario_distancia.keys():
            if e not in lista_distancia:
                lista_distancia.append(e)
        lista_distancia.sort()
        print('Distâncias: ')
        for di in lista_distancia:
            if di >= 10000:
                print(cor(166, 43, 237,f'    {di:.2f} KM -> {dicionario_distancia[di]}'))
            elif di < 10000 and di >= 5000:
                print(cor(237, 211, 43,f'    {di:.2f} KM -> {dicionario_distancia[di]}'))
            elif di < 5000 and di >= 1000:
                print(cor(92, 237, 43,f'    {di:.2f} KM -> {dicionario_distancia[di]}'))
            elif di < 1000:
                print(cor(41, 240, 193,f'    {di:.2f} KM -> {dicionario_distancia[di]}'))
    
    if pais == "inventario":
        if inventario == {}:
            print('Seu inventário está vazio.')
        else:
            for e in inventario.keys():
                print(f'{e} --> {inventario[e]}')
            
    if pais == 'dica':
        print('----------------------------------------')
        for e, dica in dic_dicas.items():
            if tentativas > custo_dicas[e]:
                print(dic_dicas[e])
        print('----------------------------------------')

        dica = int(input(f'Escolha sua opção: '))

        if dica >= 7 or dica not in lista_dicas: 
            print('Por favor, escolha uma dica que esteja no mercado.')

        elif dica == 1 and dica in lista_dicas: 
            cor_pais = cor_predominante(bandeira)
            print(f'A cor predominante da bandeira é: {cor_pais}')
            tentativas -= 4
            numero_tentativas = tentativas - tentativas_u
            inventario['Cor da bandeira: '] = cor_pais
            del dic_dicas[1]
            del lista_dicas[0]

        elif dica == 2 and dica in  lista_dicas: 
            x=0
            if tentativas < 3:  
                print('Você não pode comprar essa dica.')
            else:
                cap += capital[x]
                print(f'Letras obtidas por enquanto: {cap}')
                tentativas -= 3
                numero_tentativas = tentativas - tentativas_u
                x+=1
                inventario['Letras da capital: '] = cap
                if len(capital)-1 == x:
                    del lista_dicas[1]
                    del dic_dicas[2]
                    

        elif dica == 3 and dica in  lista_dicas: 
            print(f'A área do país é: {area}')
            del dic_dicas[3]
            tentativas -= 6
            numero_tentativas = tentativas - tentativas_u
            del lista_dicas[2]
            inventario['Área do país: '] = area
            

        elif dica == 4 and dica in  lista_dicas: 
            print(f'{populacao} pessoas.')
            tentativas -= 5
            numero_tentativas = tentativas - tentativas_u
            inventario['População'] = populacao
            del lista_dicas[3]
            del dic_dicas[4]
            

        elif dica == 5 and dica in  lista_dicas: 
            print(f'Está no continente: {continente}')
            tentativas -= 7
            numero_tentativas = tentativas - tentativas_u
            inventario['Continente'] = continente
            del lista_dicas[4]
            del dic_dicas[5]
            

        elif dica == 6: 
            print('\n\nVoltando ao jogo!\n\n')

    
        if tentativas > 10:
            print(f'Tentativas restantes:', f'\033[0;32m {tentativas}\033[0;0m')
        elif tentativas <= 10 and tentativas > 5:
            print(f'Tentativas restantes:', f'\033[0;33m {tentativas}\033[0;0m')
        elif tentativas <= 5:
            print(f'Tentativas restantes:', f'\033[0;31m {tentativas}\033[0;0m')

    if pais == pais_escolhido:
        print(f'Parabéns! Você adivinhou o país "{pais_escolhido}" em {tentativas_u} tentativas!')
        print('Finalizando jogo...')
        jogar_novamente = False
        tentativas = 0
        pais_escolhido = sorteia_pais(dicionário_paises)
        jogar_novamente = input('Deseja jogar novamente? [s|n] ')
        if jogar_novamente == 'n':
            jogar_novamente = False
            print('\nAté a próxima!')
            break
        elif jogar_novamente == 's':
            lista_distancias = []
            lista_dist_colorido = []
            lista_tentativas = []
            lista_dicas = [1,2,3,4,5,6]
            capital_str = ''
            inventario = {}
            dic_distancia = {}
            indice_pais = 1
            c = 0 
            d = 0
            lista1= []
            dicionario_distancia = {}
            lista_distancia = []
            x=0
            i=0
            ok = False
            inventario = {}
            dic_distancia = {}
            cap= ''
            lista_distancias = []
            jogar_novamente = True 
            lista_dist_colorido = []
            lista_dicas = [1,2,3,4,5,6]
            area = (dicionário_paises[pais_escolhido])['area']
            populacao = (dicionário_paises[pais_escolhido])['populacao']
            capital = (dicionário_paises[pais_escolhido])['capital']
            latitude = ((dicionário_paises[pais_escolhido])['geo'])['latitude']
            longitude = ((dicionário_paises[pais_escolhido])['geo'])['longitude']
            bandeira = (dicionário_paises[pais_escolhido])['bandeira']
            continente = (dicionário_paises[pais_escolhido])['continente']
        
    if tentativas == 0:
        print(f'Infelizmente suas tentativas acabaram! O país era "{pais_escolhido}"!')
        print('Finalizando jogo...')
        jogar_novamente = False
        tentativas = 0
        pais_escolhido = sorteia_pais(dicionário_paises)
        jogar_novamente = input('Deseja jogar novamente? [s|n] ')
        if jogar_novamente == 'n':
            jogar_novamente = False
            print('\nAté a próxima!')
            break
        elif jogar_novamente == 's':
            lista_distancias = []
            lista_dist_colorido = []
            lista_tentativas = []
            lista_dicas = [1,2,3,4,5,6]
            capital_str = ''
            inventario = {}
            dic_distancia = {}
            indice_pais = 1
            c = 0 
            d = 0
            lista1= []
            dicionario_distancia = {}
            lista_distancia = []
            x=0
            i=0
            ok = False
            inventario = {}
            dic_distancia = {}
            cap= ''
            lista_distancias = []
            jogar_novamente = True 
            lista_dist_colorido = []
            lista_dicas = [1,2,3,4,5,6]
            area = (dicionário_paises[pais_escolhido])['area']
            populacao = (dicionário_paises[pais_escolhido])['populacao']
            capital = (dicionário_paises[pais_escolhido])['capital']
            latitude = ((dicionário_paises[pais_escolhido])['geo'])['latitude']
            longitude = ((dicionário_paises[pais_escolhido])['geo'])['longitude']
            bandeira = (dicionário_paises[pais_escolhido])['bandeira']
            continente = (dicionário_paises[pais_escolhido])['continente']

        if jogar_novamente != 'n' or jogar_novamente != 's':
            while jogar_novamente != 'n' or jogar_novamente != 's':
                jogar_novamente = input('Escolha uma opção válida, deseja jogar novamente? [s|n] ')
                if jogar_novamente == 'n':
                    jogar_novamente = False
                    print('Até a próxima!')
                    break
                elif jogar_novamente == 's':
                    lista_distancias = []
                    lista_dist_colorido = []
                    lista_tentativas = []
                    lista_dicas = [1,2,3,4,5,6]
                    capital_str = ''
                    inventario = {}
                    dic_distancia = {}
                    indice_pais = 1
                    c = 0 
                    d = 0
                    area = (dicionário_paises[pais_escolhido])['area']
                    populacao = (dicionário_paises[pais_escolhido])['populacao']
                    capital = (dicionário_paises[pais_escolhido])['capital']
                    latitude = ((dicionário_paises[pais_escolhido])['geo'])['latitude']
                    longitude = ((dicionário_paises[pais_escolhido])['geo'])['longitude']
                    bandeira = (dicionário_paises[pais_escolhido])['bandeira']
                    continente = (dicionário_paises[pais_escolhido])['continente']
                    lista1= []
                    dicionario_distancia = {}
                    lista_distancia = []
                    x=0
                    i=0
                    ok = False
                    inventario = {}
                    dic_distancia = {}
                    cap= ''
                    lista_distancias = []
                    jogar_novamente = True 
                    lista_dist_colorido = []
                    lista_dicas = [1,2,3,4,5,6]


    
    if pais == 'desisto':
        desistir = input('Deseja mesmo desistir? [s|n]: ')
        if desistir == 's':
            print('Quem sabe na próxima!\nFinalizando jogo...')
            print('Fim de jogo!')
            print(f'O país sorteado era {pais_escolhido}!')
            jogar_novamente = False
            tentativas = 0
        elif desistir == 'n':
            print('Voltando ao jogo...')


        pais_escolhido = sorteia_pais(dicionário_paises)
        jogar_novamente = input('Deseja jogar novamente? [s|n] ')
        if jogar_novamente == 'n':
            jogar_novamente = False
            print('\nAté a próxima!')
            break
        elif jogar_novamente == 's':
            lista_distancias = []
            lista_dist_colorido = []
            lista_tentativas = []
            lista_dicas = [1,2,3,4,5,6]
            capital_str = ''
            inventario = {}
            dic_distancia = {}
            indice_pais = 1
            c = 0 
            d = 0
            area = (dicionário_paises[pais_escolhido])['area']
            populacao = (dicionário_paises[pais_escolhido])['populacao']
            capital = (dicionário_paises[pais_escolhido])['capital']
            latitude = ((dicionário_paises[pais_escolhido])['geo'])['latitude']
            longitude = ((dicionário_paises[pais_escolhido])['geo'])['longitude']
            bandeira = (dicionário_paises[pais_escolhido])['bandeira']
            continente = (dicionário_paises[pais_escolhido])['continente']
            lista1= []
            dicionario_distancia = {}
            lista_distancia = []
            x=0
            i=0
            ok = False
            inventario = {}
            dic_distancia = {}
            cap= ''
            lista_distancias = []
            jogar_novamente = True 
            lista_dist_colorido = []
            lista_dicas = [1,2,3,4,5,6]

        if jogar_novamente != 'n' or jogar_novamente != 's':
            while jogar_novamente != 'n' or jogar_novamente != 's':
                jogar_novamente = input('Escolha uma opção válida, deseja jogar novamente? [s|n] ')
                if jogar_novamente == 'n':
                    jogar_novamente = False
                    print('Até a próxima!')
                    break
                elif jogar_novamente == 's':
                    lista_distancias = []
                    lista_dist_colorido = []
                    lista_tentativas = []
                    lista_dicas = [1,2,3,4,5,6]
                    capital_str = ''
                    inventario = {}
                    dic_distancia = {}
                    indice_pais = 1
                    c = 0 
                    d = 0
                    area = (dicionário_paises[pais_escolhido])['area']
                    populacao = (dicionário_paises[pais_escolhido])['populacao']
                    capital = (dicionário_paises[pais_escolhido])['capital']
                    latitude = ((dicionário_paises[pais_escolhido])['geo'])['latitude']
                    longitude = ((dicionário_paises[pais_escolhido])['geo'])['longitude']
                    bandeira = (dicionário_paises[pais_escolhido])['bandeira']
                    continente = (dicionário_paises[pais_escolhido])['continente']
                    lista1= []
                    dicionario_distancia = {}
                    lista_distancia = []
                    x=0
                    i=0
                    ok = False
                    inventario = {}
                    dic_distancia = {}
                    cap= ''
                    lista_distancias = []
                    jogar_novamente = True 
                    lista_dist_colorido = []
                    lista_dicas = [1,2,3,4,5,6]
