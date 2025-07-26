import pygame
from pygame.locals import * # Importa todas as constantes e funções úteis
from sys import exit  # Importa a função exit para fechar o programa
from random import randint  # Importa randint para gerar números aleatórios

# Inicializar o Pygame
pygame.init()
musica_fundo = pygame.mixer.music.load('BoxCat_Games_-_08_-_CPU_Talk.ogg.mp3')  # Carrega a música de fundo
pygame.mixer.music.play(-1)  # Toca a música em loop (-1 significa que tocará indefinidamente)
# Definindo as dimensões da tela
colisao_som = pygame.mixer.Sound('smw_coin.wav')  # Carrega o som de colisão
pygame.mixer.music.set_volume(0.1)  # Define o volume da música de fundo
largura = 640
altura = 480

x_cobra = int(largura/2) # x e y irão alterar dando a senssação de movimento - lagura/2 faz com que nosso quadro inicie no meio da tela
y_cobra = (altura/2) # tão serão inseridas na tupla de posção do objeto para provocar a variação de posição dele na tela
# Criando a janela do

velocidade = 10
x_controle = velocidade  # Variável para controle do movimento no eixo X
y_controle = 0  # Variável para controle do movimento no eixo y

x_maca = randint(40, 600)  # Posição aleatória do retângulo azul
y_maca = randint(50, 430)  # Posição aleatória do retângulo azul

pontos = 0
fonte = pygame.font.SysFont('arial', 20, True, True) # Fonte do texto que será exibido na tela(tipo, tamanho, negrito, italico, etc)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('SNAKE')  # Opcional: título da janela
relogio = pygame.time.Clock() # Objeto que irá orientar a velocidade do jogo
lista_cobra = []
comprimento_inicial = 5 # Comprimento inicial da cobra
fim_jogo = False  # Variável para controlar o fim do jogo

def aumenta_cobra(lista_cobra):
    for xey in lista_cobra:
        pygame.draw.rect(tela, (100, 150, 75), (xey[0], xey[1], 20, 20))


def reiniciar_jogo():
    global x_cobra, y_cobra, x_maca, y_maca, pontos, comprimento_inicial, lista_cobra, lista_cabeca, fim_jogo
    pontos = 0
    comprimento_inicial = 5
    x_cobra = int(largura/2)
    y_cobra = (altura/2)
    lista_cobra = []
    lista_cabeca = []
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    fim_jogo = False


# Loop principal do jogo
while True:
    relogio.tick(30) # Frames por segundo do jogo
    tela.fill((255,255,255)) # Esse comando limpa a tela, trazendo a tela para uma cor neutra sem a presença do nosso bloco
    mensagem = f'Pontos: {pontos}'  # Mensagem que será exibida na tela com a quantidade de pontos
    texto_formatado = fonte.render(mensagem, True, (0,0,0))  # Renderiza o texto com a fonte definida   (variável, anti-aliasing, cor)
    for event in pygame.event.get():  # Verifica todos os eventos
        if event.type == QUIT:        # Se clicar no botão de fechar
            pygame.quit()             # Finaliza o pygame
            exit()                    # Encerra o programa

        if event.type == KEYDOWN:
            if event.key == K_a: # Move o objeto a esquerda removendo valor do eixo de X
                if x_controle == velocidade:  # Impede que a cobra se mova na direção oposta imediatamente
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d: # Move o objeto a direita acrescentando valor do eixo de X
                if x_controle == -velocidade:  # Impede que a cobra se mova na direção oposta imediatamente
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w: # Move o objeto para superior removendo valor do eixo de Y
                if y_controle == velocidade:  # Impede que a cobra se mova na direção oposta imediatamente
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_s: # Move o objeto para inferior acrescentando valor do eixo de Y
                if y_controle == -velocidade:  # Impede que a cobra se mova na direção oposta imediatamente
                    pass
                else:
                    x_controle = 0
                    y_controle = velocidade
                
    x_cobra += x_controle  # Atualiza a posição do objeto no eixo X
    y_cobra += y_controle  # Atualiza a posição do objeto no eixo Y 

    cobra = pygame.draw.rect(tela, (100, 150, 75),(x_cobra,y_cobra,20,20)) #Quadrado - (tela,(R,G,B),(x,y,largura,altura))
    maca = pygame.draw.rect(tela, (255, 100, 100),(x_maca,y_maca,20,20)) #Quadrado - (tela,(R,G,B),(x,y,largura,altura))

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)  # Após a colizão reposiciona o retângulo azul aleatoriamente
        y_maca = randint(50, 430)   # Após a colizão reposiciona o retângulo azul aleatoriamente
        pontos += 1 # Dentro do loop principal do jogo, a cada colisão com o retângulo azul, incrementa 1 ponto
        colisao_som.play() # Toca o som de colisão
        comprimento_inicial += 1  # Aumenta o comprimento da cobra a cada colisão

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        fonte2 = pygame.font.SysFont('arial', 15, True, True) # Fonte do texto que será exibido na tela(tipo, tamanho, negrito, italico, etc)
        mensagem_fim = 'Fim de Jogo! Pressione R para reiniciar'
        texto_fim = fonte2.render(mensagem_fim, True, (0,0,0))
        ret_texto = texto_fim.get_rect() # Cria um retângulo para o texto formatado
        fim_jogo = True
        while fim_jogo:
            tela.fill((255,255,255)) # Limpa a tela
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()
            ret_texto.center = (largura//2, altura//2) # Centraliza o retângulo do texto formatado na tela
            tela.blit(texto_fim, ret_texto) # Desenha o texto formatado na tela
            pygame.display.update() # Atualiza a tela
    
    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura
                      
    if len(lista_cobra) > comprimento_inicial:  # Se o comprimento da cobra for maior que o comprimento inicial
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)  # Chama a função que desenha a cobra na tela


    tela.blit(texto_formatado, (530, 10))  # Desenha o texto formatado na tela na posição (10, 10)
    pygame.display.update() # Atualiza o conteúdo da tela
