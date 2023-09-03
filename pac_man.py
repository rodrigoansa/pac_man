import pygame
import constantes
import sprites

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((constantes.largura, constantes.altura))
        pygame.dispay.set_caption(constantes.nome_jogo)
        self.relogio = pygame.time.Clock()
        self.rodando = True

    def novo_jogo(self):
        self.todas_sprites = pygame.sprite.Group()
        self.rodar()

    def rodar(self):
        self.jogando = True
        while self.jogando:
            self.relogio.tick(constantes.fps)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()

    def eventos(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                self.esta_rodando = False