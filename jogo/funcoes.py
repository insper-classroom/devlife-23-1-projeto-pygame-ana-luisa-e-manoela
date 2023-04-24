import pygame
pygame.init()

def inicializa():
    assets = {

    }
    window = pygame.display.set_mode((1000, 450), vsync=True, flags=pygame.SCALED)
    state = {
        'pos_brock': [990, 440], 
    }
    return window, assets, state

def desenha(window, assets, state):
    fundo_jogo = pygame.image.load("docs\imagens\download.png")
    fundo_jogo = pygame.transform.scale(fundo_jogo, (1000, 450))
    window.blit(fundo_jogo, (0,0)) 
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
