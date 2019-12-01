import pygame
from player import Player
import env
from spritesheet import Spritesheet
import maze

pygame.init()

window_size = env.WINDOW_SIZE

screen = pygame.display.set_mode(window_size)
running = True

spritesheet = Spritesheet()

player_sprite = spritesheet.sprite_at(4, 8)
wall_sprite = spritesheet.sprite_at(0, 1)
floor_sprite = spritesheet.sprite_at(4, 6)

player = Player(player_sprite, 32, 32)
player_speed = 2

fps = int(1000 / 60)

level = maze.generate_maze(env.LEVEL_W, env.LEVEL_H)


def user_input():
	global running
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			running = False
		elif ev.type == pygame.KEYDOWN:
			if ev.key == pygame.K_q:
				running = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT]:
		player.x -= player_speed
	if keys[pygame.K_RIGHT]:
		player.x += player_speed
	if keys[pygame.K_UP]:
		player.y -= player_speed
	if keys[pygame.K_DOWN]:
		player.y += player_speed


def update():
	pass


def render():
	screen.fill((34, 34, 34))
	for y in range(env.LEVEL_H):
		for x in range(env.LEVEL_W):
			if level[y * env.LEVEL_W + x] == 1:
				screen.blit(wall_sprite, (x * env.BLOCK_SIZE[0], y * env.BLOCK_SIZE[1]))
			elif level[y * env.LEVEL_W + x] == 0:
				screen.blit(floor_sprite, (x * env.BLOCK_SIZE[0], y * env.BLOCK_SIZE[1]))

	player.blit(screen)
	pygame.display.update()


def check_colision(x1, y1, x2, y2, size):
	return x2 <= x1 < x2 + size and y2 <= y1 <= y2 + size


while running:
	user_input()
	update()
	render()
	pygame.time.wait(fps)
