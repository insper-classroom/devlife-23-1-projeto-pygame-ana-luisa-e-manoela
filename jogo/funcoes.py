import pygame
pygame.init()

def inicializa():
    assets = {
        'brock' : pygame.image.load("docs/imagens/personagem.png"), 
        'caixa' : pygame.image.load("docs/imagens/caixa angry birds.png"),
        'estilingue' : pygame.image.load("docs/imagens/estilingue.png"),
        'bulbasaur' : pygame.image.load("docs/imagens/planta dino.png"), 
        'clefairy' : pygame.image.load("docs/imagens/clefairy.png"),
        'estrelinha' : pygame.image.load("docs/imagens/estrelinha.png"),
        'eevee' : pygame.image.load("docs/imagens/leaozinho.png"), 
        'pikachu' : pygame.image.load("docs/imagens/pikachu.png"), 
        'mimikyu' : pygame.image.load("docs/imagens/mimikyu.png"),
        'pokebola' : pygame.image.load("docs/imagens/pokebola.png"),
        'exclamação' : pygame.image.load("docs/imagens/exclamação.png"),
        'snorlax' : pygame.image.load("docs/imagens/snorlax.png"),
        'fofopreto' : pygame.image.load("docs/imagens/cachorro].png"),
        'rosinha' : pygame.image.load("docs/imagens/meufav.png"),
        'passaro azul' : pygame.image.load("docs/imagens/passro azul.png"),
        'rato' : pygame.image.load("docs/imagens/sato.png"),
        'corações': pygame.image.load("docs/imagens/corações.png"),
        'tnt' : pygame.image.load("docs/imagens/surpresa.png"),
        'dragao branco' : pygame.image.load("docs/imagens/dragao branco.png"),
        'passaro vila sesamo' : pygame.image.load("docs/imagens/urubu amarelo.png"),

    }

    window = pygame.display.set_mode((1000, 450), vsync=True, flags=pygame.SCALED)
    pygame.mixer.music.load("docs/musica/sound.mp3")
    pygame.mixer.music.play() 
    state = {
    }

    return window, assets, state

def desenha(window, assets, state):

    fundo_jogo = pygame.image.load("docs/imagens/download.png")
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
    assets['exclamação'] = pygame.transform.scale(assets['exclamação'], (45,45))
    assets['snorlax'] = pygame.transform.scale(assets['snorlax'], (50,50))
    assets['fofopreto'] = pygame.transform.scale(assets['fofopreto'], (45,45))
    assets['rosinha'] = pygame.transform.scale(assets['rosinha'], (40,40))
    assets['passaro azul'] = pygame.transform.scale(assets['passaro azul'], (70,60))
    assets['rato'] = pygame.transform.scale(assets['rato'], (40,40))
    assets['corações'] = pygame.transform.scale(assets['corações'], (20,20))
    assets['tnt'] = pygame.transform.scale(assets['tnt'], (40,40))
    assets['dragao branco'] = pygame.transform.scale(assets['dragao branco'], (50,50))
    assets['passaro vila sesamo'] = pygame.transform.scale(assets['passaro vila sesamo'], (100,100)) 
    


    window.blit(fundo_jogo, (0,0)) 
    window.blit(assets['bulbasaur'], ((865, 289)))
    window.blit(assets['brock'], ((5, 250)))
    window.blit(assets['estilingue'], ((100, 320)))
    window.blit(assets['clefairy'], ((925, 289)))
    window.blit(assets['estrelinha'], ((810, 297)))
    window.blit(assets['eevee'], ((843, 234)))
    window.blit(assets['pikachu'], ((886, 233)))
    window.blit(assets['mimikyu'], ((870, 173)))
    window.blit(assets['pokebola'], ((110, 325)))
    window.blit(assets['exclamação'], ((40, 210)))
    window.blit(assets['snorlax'], ((587, 285)))
    window.blit(assets['fofopreto'], ((528, 295)))
    window.blit(assets['rosinha'], ((563, 235)))
    window.blit(assets['passaro azul'], ((700, 75)))
    window.blit(assets['rato'], ((319,295)))
    window.blit(assets['corações'], ((5, 400)))
    window.blit(assets['corações'], ((20, 400)))
    window.blit(assets['corações'], ((35, 400)))
    window.blit(assets['tnt'], ((690, 310)))
    window.blit(assets['tnt'], ((420, 310)))
    window.blit(assets['dragao branco'], ((600, 20)))
    window.blit(assets['passaro vila sesamo'], ((400, 40)))



    caixas = [(800, 285), (860, 285), (920, 285), (830, 226), (890, 226), (860, 167), (580, 285), (520, 285), (548, 226), (310, 285)]
    for i in caixas:
        window.blit(assets['caixa'], (i))

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
