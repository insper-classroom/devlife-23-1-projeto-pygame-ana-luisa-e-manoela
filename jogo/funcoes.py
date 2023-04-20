import pygame

def inicializa():
    assets = {

    }
    pygame.init()
    window = pygame.display.set_mode((1000, 450), vsync=True, flags=pygame.SCALED)
    state = {

    }
    return assets, window, state
