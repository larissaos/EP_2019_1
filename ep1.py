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
                "inicio": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual


def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]
        
        caracteres = "-"*len(nome_cenario_atual)
        
        print ("você está em:\n{0}\n{1}\n {2}".format(nome_cenario_atual, caracteres, cenarios))
        
        opcoes = cenario_atual['opcoes']
        
       
        
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:

            # Aluno B: substitua este comentário e a linha abaixo pelo código
            # para pedir a escolha do usuário.
            escolha = ""

            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
