import pygame
pygame.init()

def inicializa():
    assets = {
        'brock' : pygame.image.load("docs\imagens\personagem.png"), 
        'caixas' : pygame.image.load("docs\imagens\caixa angry birds.png")

    }

    window = pygame.display.set_mode((1000, 450), vsync=True, flags=pygame.SCALED)
    state = {

    }

    return window, assets, state

def desenha(window, assets, state):
    fundo_jogo = pygame.image.load("docs\imagens\download.png")
    fundo_jogo = pygame.transform.scale(fundo_jogo, (1000, 450))
    assets['brock'] = pygame.transform.scale(assets['brock'], (120,120))
    assets['caixas'] = pygame.transform.scale(assets['caixas'], (60, 60)) 
    window.blit(fundo_jogo, (0,0)) 
    window.blit(assets['brock'], ((5, 250)))
    window.blit(assets['caixas'], ((800, 285)))

    pygame.display.update()

def recebe_eventos():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit() 

if __name__ == '__main__':
    window, assets, state = inicializa()
    desenha(window, assets, state)
    recebe_eventos()
