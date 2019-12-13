import pygame

import maze
import spritesheet
import env
from player import Player
import random

pygame.init()

window_size = (1024, 768)
w = env.WINDOW_SIZE[0] // env.BLOCK_SIZE[0]
h = env.WINDOW_SIZE[1] // env.BLOCK_SIZE[0]

level = [1] * (w * h)
for x in range(1, w, 2):
	for y in range(1, h, 2):
		maze.carve_maze(level, w, h, x, y)

window = pygame.display.set_mode(window_size)

grey = (200, 200, 200)

running = True

fps = 1000 // 69

sheet = spritesheet.Spritesheet()

player_sprite = sheet.sprite_at(4, 8)
wall_sprite = sheet.sprite_at(0, 1)
exit_sprite = sheet.sprite_at(8, 14)
player = Player(player_sprite, 1, 1)


# CTRL ALT L
def generate_exit(m, width, height):
	ex = 0
	ey = 0
	while m[ey * width + ex] == 1:
		ex = random.randint(1, width - 3)
		ey = random.randint(1, height - 3)
	return [ex, ey]

exit_coords = generate_exit(level, h, w)
level[exit_coords[1] * w + exit_coords[0]] = 2
print(exit_coords)

def user_input():
	global running, player_pos
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			running = False
		elif ev.type == pygame.KEYDOWN:
			if ev.key == pygame.K_q:
				running = False

	keys = pygame.key.get_pressed()

	if keys[pygame.K_LEFT]:
		if level[player.y * w + player.x - 1] == 0:
			player.move(Player.PlayerDir.LEFT)
	if keys[pygame.K_RIGHT]:
		if level[player.y * w + player.x + 1] == 0:
			player.move(Player.PlayerDir.RIGHT)
	if keys[pygame.K_UP]:
		if level[(player.y - 1) * w + player.x] == 0:
			player.move(Player.PlayerDir.UP)
	if keys[pygame.K_DOWN]:
		if level[(player.y + 1) * w + player.x] == 0:
			player.move(Player.PlayerDir.DOWN)


def render():
	window.fill(grey)
	for x in range(0, w):
		for y in range(0, h):
			block = level[y * w + x]
			if block == 1:
				window.blit(wall_sprite, (x * env.BLOCK_SIZE[0], y * env.BLOCK_SIZE[1]))
			elif block == 2:
				window.blit(exit_sprite, (x * env.BLOCK_SIZE[0], y * env.BLOCK_SIZE[1]))

	player.blit(window)
	pygame.display.update()


def update():
	pass


def check_collision(x1, y1, x2, y2, size):
	return x2 <= x1 < x2 + size and y2 <= y1 < y2 + size


while running:
	user_input()
	update()
	render()
	pygame.time.wait(fps)
