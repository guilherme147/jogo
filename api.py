import PySimpleGUI as sg
import random
sg.theme('DarkAmber')
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
                    sg.popup('Vez do jogador', jogador, title='Jogo') 
                    sorteio = random.randint(1, 6)
                    i['posicao'] += sorteio
                    sg.popup("Saiu no dado {sorteio}", i['posicao'], title='Jogo')
                    i['posicao'] = cartas(jogador, i['posicao'])
                if(i['posicao'] >= 51):
                    ganhador = jogador
                    terminaJogo(ganhador)
def adicionarJogador(jogadores, icon):
    layout = [
        [sg.Text('Deseja adicionar outro jogador?')],
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
                criaJogadores(jogadores, icon)
                break
        if(event == 'Jogar'):
            if(len(jogadores) < 2):
                sg.popup_error("Ocorreu um erro! Para jogar deve ter no minimo 2 jogadoores", title="Erro")
                criaJogadores(jogadores, icon)
                break
            else:
                comecarJogo(jogadores)
                break
    window.close()
def criaJogadores(jogadores, icon):
    # layout
    layout = [
        [sg.Text('Digite o seu nome'), sg.InputText()],
        [sg.Combo(icon, 'Escolha um icon', s=(15,22), enable_events=True)],
        [sg.Text('Digite sua senha'), sg.InputText(password_char='*')],
        [sg.Button('OK'), sg.Button('Cancelar')]
    ]
    # janela
    window = sg.Window('registro', layout)
    # funcionamento
    while a == True:
        event, values = window.read()
        valor1 = values[0]
        valor2 = values[2]
        print(valor1)
        if(event == sg.WIN_CLOSED or event == 'Cancelar'):
            break
        if(event == 'OK'):
            jogadores.append({"nome": valor1, "senha": valor2, "icon": values[1], "posicao": 0})
            print(jogadores)
            window.close()
            adicionarJogador(jogadores, icon)
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
        print("O jogador", nome , " ganhou uma carta e devera avançar 3 casas")
        posicao += 3
    elif(posicao == 9):
        print("O jogador", nome , " ganhou uma carta e devera escolher um jogador para voltar 3 casas")
        posicao -= 3
    elif(posicao == 14):
        print("O jogador", nome , " ganhou uma carta e devera voltar 1 casa")
        posicao -= 1
    elif(posicao == 16):
        print("O jogador", nome , " ganhou uma carta e devera escolher um jogador para voltar 2 casas")
        posicao += 3
    elif(posicao == 21):
        print("O jogador", nome , " ganhou uma carta e devera voltar ao inicio")
        posicao = 0
    elif(posicao == 27):
        print("O jogador", nome , " ganhou uma carta e devera avancar 3 casas")
        posicao += 3
    elif(posicao == 33):
        print("O jogador", nome , " ganhou uma carta e devera escolher um jogador para voltar 3 casas")
        posicao -= 3
    elif(posicao == 37):
        print("O jogador", nome , " ganhou uma carta e devera avancar 4 casas")
        posicao += 4
    elif(posicao == 39):
        print("O jogador", nome , " ganhou uma carta e devera voltar 1 casa")
        posicao -= 1
    elif(posicao == 40):
        print("O jogador", nome , " ganhou uma carta e devera escolher um jogador para avancar 2 casas")
        posicao += 3
    elif(posicao == 43):
        print("O jogador", nome , " ganhou uma carta e devera avancar 1 casa")
        posicao += 1
    elif(posicao == 45):
        print("O jogador", nome , " ganhou uma carta e devera voltar 3 casas")
        posicao -= 3    
    elif(posicao == 45):
        print("O jogador", nome , " ganhou uma carta e devera voltar 2 casas")
        posicao -= 2
    elif(posicao == 49):
        print("O jogador", nome , " ganhou uma carta e devera escolher um jogador para avancar 3 casas")
        posicao += 3        
jogadores = []   
icon = [":D", ":)", ":|", ":(", ";("]
a = True
criaJogadores(jogadores, icon)