import pygame
import env


class Spritesheet(object):
	def __init__(self) -> None:
		super().__init__()
		self.spritesheet = pygame.image.load(env.SPRITE_IMAGE).convert_alpha()

	def sprite_at(self, x, y):
		rect = pygame.Rect((x * env.SPR_SIZE[0], y * env.SPR_SIZE[1], env.SPR_SIZE[0], env.SPR_SIZE[1]))
		image = pygame.Surface(env.SPR_SIZE, pygame.SRCALPHA)
		image.blit(self.spritesheet, (0, 0), rect)
		return pygame.transform.scale(image, env.BLOCK_SIZE)

