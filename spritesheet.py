import pygame
import env

# klasa za importovanje teksturas
class Spritesheet(object):
	def __init__(self) -> None:
		super().__init__()
		# ucitavamo ceo PNG fajl u memoriju
		self.spritesheet = pygame.image.load(env.SPRITE_IMAGE).convert_alpha()

	# ucitavamo specificni spirte iz naseg sprite grid-a
	def sprite_at(self, x, y):
		# definisemo velicinu sprite-a 16 x 16 (velicina kao u fajlu) i njegovu lokaciju (x i y) na gridu
		rect = pygame.Rect((x * env.SPR_SIZE[0], y * env.SPR_SIZE[1], env.SPR_SIZE[0], env.SPR_SIZE[1]))
		# kreiramo "Surface" koji ce da cuva nasu teksturu
		image = pygame.Surface(env.SPR_SIZE, pygame.SRCALPHA)
		# kopiramo teksturu iz sprite grid-a
		image.blit(self.spritesheet, (0, 0), rect)
		# vracamo uvecanu teksturu (16x16) -> (32x32)
		return pygame.transform.scale(image, env.BLOCK_SIZE)

