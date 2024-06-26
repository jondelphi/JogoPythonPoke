import pygame
from abertura import Abertura
from principal import Principal
from fim import Fim
from recordes import Recordes

def guardarecordes(arquivo):
    recordes = list()
    with open(arquivo, "r") as r:
        for _ in r:
            texto = _.strip()
            recordes.append(texto)
    r.close()
    nome=list()
    for i in range (0, len(recordes)):
        if i % 3 ==0:
            nome.append(recordes[i])  
    data=list()
    for i in range (1, len(recordes),3):
        data.append(recordes[i])  
    poke=list()
    for i in range (2, len(recordes),3):
        poke.append(recordes[i])  
    valores = dict()
    for l in range(5):
        valores[l+1]=[nome[l], data[l],poke[l]]    
    dicionario_organizado = dict(sorted(valores.items(), key=lambda item: int(item[1][2]), reverse=True))
    return(dicionario_organizado)




pygame.init()

rodando = True
funcao = "abertura"

while rodando:
    if funcao == "abertura":
        abre = Abertura()
        abre.abre("abre.jpg", "Início do Game")
        funcao = abre.funcao
    elif funcao == "principal":
        principal = Principal()
        principal.run_principal("bg.jpg", "Jogando PokeBolas")
        funcao = principal.funcao
    elif funcao == "fim":
        fim = Fim()
        fim.abre("fim.jpg", "Jogando PokeBolas")
        funcao = fim.funcao
    elif funcao == "recordes":
        recordes = Recordes()
        recordes.abre("Melhores Jogadores")
        funcao = recordes.funcao
    pygame.display.flip()
