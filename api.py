import PySimpleGUI as sg
import random
sg.theme('LightGrey1')
def comecarJogo(jogadores):
    layout = [
        [sg.Image("image.png", key='-BACKGROUND-', enable_events=True)],
        [sg.Button(image_filename="dado.png", size=(10, 10), key='sorteio')]
    ]
    window = sg.Window('jogo', layout)
    while a == True:
        event, values = window.read()
        if(event == sg.WIN_CLOSED or event == 'Cancelar'):
            break
        while(True):
            for i in jogadores:
                jogador = i['nome']
                if(event == 'sorteio'):
                    sg.popup(f"Vez do jogador {jogador}", title='Jogo') 
                    sorteio = random.randint(1, 6)
                    i['posicao'] = i['posicao'] + sorteio
                    sg.popup(f"O dado sorteou o numero {sorteio}", f"O jogador está na posição {i['posicao']}", title='Jogo')
                    if((cartas(jogador, i['posicao'])) > i['posicao']):
                        i['posicao'] = cartas(jogador, i['posicao'])
                        sg.popup(f"O {i['nome']} tirou uma carta e avançou para posição {i['posicao']}")
                    if((cartas(jogador, i['posicao'])) < i['posicao']):
                        i['posicao'] = cartas(jogador, i['posicao'])
                        sg.popup(f"O {i['nome']} tirou uma carta e voltou para posição {i['posicao']}.")
                verificador = finalizaJogo(i['posicao'])
                if(event == sg.WIN_CLOSED or event == 'Cancelar'):
                    window.close()
                    break
                if(verificador == True):
                    vencedor = jogador
                    break

            if(verificador == True):
                    window.close()
                    break
        sg.popup(f"O jogador {vencedor} ganhou o jogo!!!!", title='Jogo')
def adicionarJogador(jogadores):
    layout = [
        [sg.Text('Deseja adicionar outro jogador?'),sg.Image("alien.png", enable_events=True)],
        [sg.Button('Sim'), sg.Button('Jogar')]
    ] 
    window = sg.Window('registro', layout)

    while a == True:
        event, values = window.read()
        if(event == sg.WIN_CLOSED or event == 'Cancelar'):
            break
        if(event == 'Sim'):
            if(len(jogadores) > 4):
                sg.popup_error("Ocorreu um erro! Voce atingiu o numero maximo de 5 jogadores! \n Iniciando jogo", title="Erro")
                comecarJogo(jogadores)
                break
            else:
                criaJogadores(jogadores)
                break
        if(event == 'Jogar'):
            if(len(jogadores) < 2):
                sg.popup_error("Ocorreu um erro! Para jogar deve ter no minimo 2 jogadoores", title="Erro")
                criaJogadores(jogadores)
                break
            else:
                comecarJogo(jogadores)
                break
    window.close()
def criaJogadores(jogadores):
    # layout
    layout = [
        [sg.Text('Digite o seu nome'), sg.InputText(),sg.Image("alien.png", enable_events=True)],
        [sg.Button('OK'), sg.Button('Cancelar')]
    ]
    # janela
    window = sg.Window('registro', layout)
    # funcionamento
    while a == True:
        event, values = window.read()
        valor1 = values[0]
        print(valor1)
        if(event == sg.WIN_CLOSED or event == 'Cancelar'):
            break
        if(event == 'OK'):
            jogadores.append({"nome": valor1, "posicao": 0})
            print(jogadores)
            window.close()
            adicionarJogador(jogadores)
            break
        if (event == 'Cancelar'):
            break
    window.close()
def sorteiaNu():
    import random
    num = random.randint(1, 6)
    return num
def criaTabuleiro():
    tabuleiro = [0]
    while(len(tabuleiro) < 51):
        num = tabuleiro[-1] + 1
        tabuleiro.append(num)
        print("[",num,"]")
criaTabuleiro()
def cartas(nome, posicao):
    if(posicao == 3):
        posicao += 3
    elif(posicao == 9):
        posicao -= 3
    elif(posicao == 14):
        posicao -= 1
    elif(posicao == 16):
        posicao += 3
    elif(posicao == 21):
        posicao = 0
    elif(posicao == 27):
        posicao += 3
    elif(posicao == 33):
        posicao -= 3
    elif(posicao == 37):
        posicao += 4
    elif(posicao == 39):
        posicao -= 1
    elif(posicao == 40):
        posicao += 3
    elif(posicao == 43):
        posicao += 1
    elif(posicao == 45):
        posicao -= 3    
    elif(posicao == 48):
        posicao -= 2
    elif(posicao == 49):
        posicao += 3
    return posicao  
def finalizaJogo(posicao):
    if(posicao > 51):
        verificador = True
    else:
        verificador = False
    return verificador
jogadores = []   
a = True
criaJogadores(jogadores)