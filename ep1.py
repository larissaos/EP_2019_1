# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Larissa Oliveira, larissaos@al.insper.edu.br
# - aluno B: Kathleen da Silva Nascimento, kathleensn@al.insper.edu.br
# - aluno C: Giovanna Alves Papandrea Neves, giovannaapn@al.insper.edu.br
import json
from random import randint
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
        while aventura:
            calculo_de_chance = randint(0,100)
            
            
            cenario_atual = cenarios[nome_cenario_atual] 
            
            tamanho_inimigos = len(inimigos["inimigos"])
            
            if(cenario_atual["título"] == "O monstro do Python"):
                inimigo_id = "chefe"
            else:
                inimigo_id = str(randint(0, tamanho_inimigos-2))
            
            inimigo_atual = inimigos["inimigos"][inimigo_id]
            
            caracteres = "-"*len(cenarios[nome_cenario_atual]["título"])
            chance_de_batalha = int(cenarios[nome_cenario_atual]["chance_inimigos"])
            
            if(chance_de_batalha > calculo_de_chance):
                batalha = False
                iniciar_batalha = True
                aventura = False
            
            if(aventura == True):
                opcoes = cenario_atual['opções']
                descricao = cenario_atual['descrição']
                
                if(cenario_atual["título"] == "Laboratório de química"):
                    inventario.append("Poção")
                        
                print (cenario_atual["título"])
                print (caracteres)
                print(descricao)
                print()
                
                
                #if opcoes == andar professor:
                #    escolha_andar_prof = input("Escolha o que você vai fazer: inicio ou professor"):
                #        if escolha_andar_prof == "Tomar elevador para saguao"
                        
                if len(opcoes) == 0:
                    print("Acabaram-se suas opções!")
                    _ = input("Pressione Enter para continuar...")
                    clear()
                    batalha = False
                    iniciar_batalha = True
                    aventura = False
                else:
                    for opcao in cenario_atual["opções"]:
                        texto = cenario_atual["opções"][opcao]["texto"]
                        space = " "*(24-len(opcao))
                        print(opcao+":", end=space)
                        print(texto)
                    
                    print()
                    escolha = input("Escolha para onde você quer ir: ")
                    if escolha in opcoes:
                        clear()
                        escolha = opcoes[escolha]["cenario"]
                        nome_cenario_atual = escolha
                    else:
                        print("Sua indecisão foi sua ruína!")
                        game_over = True
                        print("Você morreu!")
                        

        while iniciar_batalha:
            i_HP = int(inimigo_atual["HP"])
            i_ATK = int(inimigo_atual["ATK"])
            i_DEF = int(inimigo_atual["DEF"])
            cenario_atual = cenarios[nome_cenario_atual] 
            caracteres = "-"*len(nome_cenario_atual)
            opcoes = cenario_atual['opções']
            descricao = cenario_atual['descrição']
            print (cenario_atual["título"])
            print (caracteres)
            print(descricao)
            print()
            print("Você encontrou um '", end="")
            print(inimigo_atual["nome"]+"'")
            print()
            print(nome_avatar+": "+str(HP)+" pontos de vida, "+str(ATK)+" pontos de ataque, "+str(DEF)+" pontos de defesa.")
            print(inimigo_atual["nome"]+": "+str(i_HP)+" pontos de vida, "+str(i_ATK)+" pontos de ataque, "+str(i_DEF)+" pontos de defesa.")
            print()
            escolha = input("Você quer 'lutar' ou 'fugir'? ")
            if(escolha == "lutar"):
                batalha = True
                aventura = False
                iniciar_batalha = False
            elif(escolha == "fugir"):
                if(cenario_atual['título'] == "O monstro do Python"):
                    print()
                    print("Você não pode fugir do Monstro Python HAHAHAHA")
                    print()
                    _ = input("Pressione enter para continuar...")
                    batalha = True
                    aventura = False
                    iniciar_batalha = False
                else:
                    print()
                    print()
                    print("Você fugiu da batalha")
                    _ = input("Pressione enter para continuar...")
                    clear()
                    aventura = True
                    batalha = False
                    iniciar_batalha = False
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
                print("Você morreu!")
                return
               
        while batalha:
            i_HP = int(inimigo_atual["HP"])
            i_ATK = int(inimigo_atual["ATK"])
            i_DEF = int(inimigo_atual["DEF"])
            
            recompensa = inimigo_atual["recompensa"]
            
            cenario_atual = cenarios[nome_cenario_atual] 
            
            caracteres = "-"*len(cenarios[nome_cenario_atual]["título"])
            
            opcoes = cenario_atual['opções']
            descricao = cenario_atual['descrição']
            print()
            print()
            while i_HP > 0 and game_over == False:
                dano = ATK-i_DEF
                i_HP = i_HP - dano
                print("Você atacou o inimigo, causando "+str(dano)+" de dano")
                if(i_HP <= 0):
                    print("Você derrotou o inimigo, e agora está com "+str(HP)+" de vida")
                    input("Pressione Enter para continuar...")
                else:
                    dano = i_ATK-DEF
                    HP = HP - dano
                    print("Você foi atacado, recebeu "+str(dano)+" de dano")
                    if(HP <= 0):
                        morrer = True
                        if(len(inventario) != 0):
                            for item in inventario:
                                if(item == "Poção"):
                                    print()
                                    print("Você consumiu sua poção")
                                    print()
                                    HP += 10
                                    inventario.remove("Poção")
                                    if(HP > 0):
                                        morrer = False
                                    else:
                                        morrer = True
                                else:
                                    morrer = True
                        else:
                            morrer = True
                            
                        if(morrer == True):
                            aventura = False
                            batalha = False
                            iniciar_batalha = False
                            game_over = True
                            print()
                            print("Você morreu em batalha")
                    
            if(i_HP <= 0):
                if(recompensa[0] == "+"):
                    ultima_letra = recompensa[len(recompensa)-1]
                    
                    if(ultima_letra == "A"):
                        ATK += int(recompensa[1:len(recompensa)-1])
                        recompensa = recompensa[0:len(recompensa)-1]+" ATK"
                    
                    elif(ultima_letra == "D"):
                        DEF += int(recompensa[1:len(recompensa)-1])
                        recompensa = recompensa[0:len(recompensa)-1]+" DEF"
                    
                    elif(ultima_letra == "H"):
                        HP += int(recompensa[1:len(recompensa)-1])
                        recompensa = recompensa[0:len(recompensa)-1]+" HP"
                elif(recompensa[0] == "%"):
                    recompensa = recompensa[1:len(recompensa)]
                    print()
                    print(recompensa)
                    game_over = True
                    return
                
                print()
                print()
                if(recompensa != ""):
                    print("Você acaba de ganhar: "+recompensa)
                input("Pressione Enter para continuar...")
                
                aventura = True
                batalha = False
                iniciar_batalha = False
                clear()
                #derrotou o monstro
        
def primeiro_texto():
    
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
    nome = input("Insira seu nome para continuar...")
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