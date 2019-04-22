# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Larissa Oliveira, larissaos@al.insper.edu.br
# - aluno B: Kathleen da Silva Nascimento, kathleensn@al.insper.edu.br
# - aluno C: Giovanna Alves Papandrea Neves, giovannaapn@al.insper.edu.br

def carregar_cenarios():
    cenarios = {
        "inicio": { #cenário 1
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": { #escolha para onde ir:
                "andar professor": "Tomar o elevador para o andar do professor", #1
                "biblioteca": "Ir para a biblioteca"#2
            }
        },
        "andar professor": {#caso escolha 1
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": { #pode escolher voltar para o inicio ou seguir na escoolha 1
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {#caso permaneça na escolha 1
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",#aqui voce morreu na escolha 1
            "opcoes": {}#depois de morrer, ressurgi na biblioteca (podemos mudar isso)
        },
        "biblioteca": {#somente uma escolha, voltar para o inicio e então precisamos criar outros cenários aqui
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {#aqui vc volta para o inicio
                "andar do professor": "Voltar para onde o monstro está",
                "subsolo": "Fugir para um lugar mais seguro"
            }
        },
        "subsolo": {
            "titulo": "Os fantasmas do laboratório",
            "descricao":"Você chegou ao subsolo."
                        "'qUEm EsTá Aí?'"
                        "Você avista três alunos fantasmas no laboratório!",
            "opcoes":{ 
                "lutar":
                "fugir"}         
            }
        },
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    cenarios, nome_cenario_atual = carregar_cenarios()#aqui deve aparecer as opções, e conforme as ecolhas

    game_over = False #se você n morreu
    while not game_over:# vc ta em algm lugar
        cenario_atual = cenarios[nome_cenario_atual] 
        
        caracteres = "-"*len(nome_cenario_atual)
        
        print ("você está em:\n{0}\n{1}\n{2}".format(nome_cenario_atual, caracteres, cenarios[nome_cenario_atual]["descricao"]))
        
        opcoes = cenario_atual['opcoes']
        
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
            print("Você morreu!")
        else:
            escolha = input("Escolha para onde você quer ir:")
            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True
                print("Você morreu!")
                
                
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
    print("Pressione Enter para continuar...")
    input()
    

    


# Programa principal.
if __name__ == "__main__":
    main()
