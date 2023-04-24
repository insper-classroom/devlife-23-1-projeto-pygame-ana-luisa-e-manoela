import pygame
pygame.init()

def inicializa():
    assets = {
        'brock' : pygame.image.load("docs\imagens\personagem.png"), 
        'caixa' : pygame.image.load("docs\imagens\caixa angry birds.png"),
        'estilingue' : pygame.image.load("docs\imagens\estilingue.png"),
        'bulbasaur' : pygame.image.load("docs\imagens\planta dino.png"), 
        'clefairy' : pygame.image.load("docs\imagens\clefairy.png"),
        'estrelinha' : pygame.image.load("docs\imagens\estrelinha.png"),
        'eevee' : pygame.image.load("docs\imagens\leaozinho.png"), 
        'pikachu' : pygame.image.load("docs\imagens\pikachu.png"), 
        'mimikyu' : pygame.image.load("docs\imagens\mimikyu.png"),
        'pokebola' : pygame.image.load("docs\imagens\pokebola.png")


    }

    window = pygame.display.set_mode((1000, 450), vsync=True, flags=pygame.SCALED)
    state = {

    }

    return window, assets, state

def desenha(window, assets, state):

    fundo_jogo = pygame.image.load("docs\imagens\download.png")
    fundo_jogo = pygame.transform.scale(fundo_jogo, (1000, 450))
    assets['brock'] = pygame.transform.scale(assets['brock'], (120,120))
    assets['caixa'] = pygame.transform.scale(assets['caixa'], (60, 60))
    assets['estilingue'] = pygame.transform.scale(assets['estilingue'], (30,50)) 
    assets['bulbasaur'] = pygame.transform.scale(assets['bulbasaur'], (50,50))
    assets['clefairy'] = pygame.transform.scale(assets['clefairy'], (55,55))
    assets['estrelinha'] = pygame.transform.scale(assets['estrelinha'], (40,45))
    assets['eevee'] = pygame.transform.scale(assets['eevee'], (45,45))
    assets['pikachu'] = pygame.transform.scale(assets['pikachu'], (70,50))
    assets['mimikyu'] = pygame.transform.scale(assets['mimikyu'], (45,45))
    assets['pokebola'] = pygame.transform.scale(assets['pokebola'], (15,15))



    window.blit(fundo_jogo, (0,0)) 
    window.blit(assets['bulbasaur'], ((865, 289)))
    window.blit(assets['brock'], ((5, 250)))
    window.blit(assets['estilingue'], ((100, 320)))
    window.blit(assets['clefairy'], ((925, 289)))
    window.blit(assets['estrelinha'], ((810, 297)))
    window.blit(assets['eevee'], ((843, 234)))
    window.blit(assets['pikachu'], ((889, 233)))
    window.blit(assets['mimikyu'], ((870, 173)))
    window.blit(assets['pokebola'], ((110, 325)))

    window.blit(assets['caixa'], ((800, 285)))
    window.blit(assets['caixa'], ((860, 285)))
    window.blit(assets['caixa'], ((920, 285)))
    window.blit(assets['caixa'], ((830, 226)))
    window.blit(assets['caixa'], ((890, 226)))
    window.blit(assets['caixa'], ((860, 167)))
 


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
