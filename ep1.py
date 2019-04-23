﻿# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Larissa Oliveira, larissaos@al.insper.edu.br
# - aluno B: Kathleen da Silva Nascimento, kathleensn@al.insper.edu.br
# - aluno C: Giovanna Alves Papandrea Neves, giovannaapn@al.insper.edu.br
import json

from os import system, name


def carregar_cenarios():
    with open('cenarios.json', encoding='utf8') as script:
        cenarios = json.load(script)
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

def carregar_inimigos():
    with open('inimigos.json', encoding='utf8') as script:
        inimigos = json.load(script)
    return inimigos


def clear(): #comando para limpar a tela, se for windows, se não, se for MAC ou Linux

    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 


def main():
    escolha = ""
    inventario = [] #lista pro inventario
    clear()
    cenarios, nome_cenario_atual = carregar_cenarios()#aqui deve aparecer as opções, e conforme as ecolhas
    inimigos = carregar_inimigos()
    nome_avatar = primeiro_texto()
    HP = 19 
    ATK = 10 
    DEF = 3 
    clear()
    game_over = False #se você n morreu
    iniciar_batalha = False 
    batalha = False 
    aventura = True 

    game_over = False #se você n morreu
    while not game_over:# vc ta em algm lugar
        cenario_atual = cenarios[nome_cenario_atual] 
        
        
        caracteres = "-"*len(nome_cenario_atual)
        
        opcoes = cenario_atual['opções']
        descricao = cenario_atual['descrição']
        
        print (cenario_atual["título"])
        print (caracteres)
        print(descricao)
        print()
        
        

        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
            print("Você morreu!")
        else:
            for opcao in cenario_atual["opções"]:
                texto = cenario_atual["opções"][opcao]["texto"]
                space = " "*(24-len(opcao))
                print(opcao+":", end=space)
                print(texto)
                
            print()
            escolha = input("Escolha para onde você quer ir:")
            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
                print("Você morreu!")
                
                
def primeiro_texto():
    print("Como quer ser chamado?")
    name = input()
    print("Na hora do sufoco!")#aqui se iniciam suas más escolhas
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()#aqui vc resolve implorar por misericódia
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()
    while(nome == "" or len(nome) < 3):
        if(nome == ""):
            clear()
            print("Todo aventureiro precisa de um nome, escolha o seu!")
            nome = input()
                
        elif(len(nome) < 3):
            clear()
            print("Esse nome é muito curto, aposto que você consegue colocar mais algumas letras nele!")
            nome = input()
    return nome



# Programa principal.
if __name__ == "__main__":
    main()