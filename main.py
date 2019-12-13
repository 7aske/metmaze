import pygame

import maze
import spritesheet
import env
from player import Player
import random

# inicijalizujemo pygame modul
pygame.init()

# visina i sirina u blokovima
w = env.WINDOW_SIZE[0] // env.BLOCK_SIZE[0]
h = env.WINDOW_SIZE[1] // env.BLOCK_SIZE[0]

# kreairamo window odgovarajucih dimenzija
window = pygame.display.set_mode(env.WINDOW_SIZE)

# generisemo level
level = [1] * (w * h)
for x in range(1, w, 2):
	for y in range(1, h, 2):
		maze.carve_maze(level, w, h, x, y)

# boja za pozadinu
#        R    G    B
grey = (200, 200, 200)

running = True

fps = 1000 // 69

# ucitavanje tekstura iz fajla
sheet = spritesheet.Spritesheet()

player_sprite = sheet.sprite_at(4, 8)
wall_sprite = sheet.sprite_at(0, 1)
exit_sprite = sheet.sprite_at(8, 14)

# kreiramo igraca iz klase player
player = Player(player_sprite, 1, 1)


# nasumicno generisemo izlaz iz lavirinta
def generate_exit(m, width, height):
	ex = 0
	ey = 0
	# sve dok je trenutni blok WALL generisemo nove vrednsti za x i y
	while m[ey * width + ex] == 1:
		ex = random.randint(1, width - 2)
		ey = random.randint(1, height - 2)
	return [ex, ey]


exit_coords = generate_exit(level, w, h)
# postavljamo exit u levels
level[exit_coords[1] * w + exit_coords[0]] = 2
print(exit_coords)


# restartujemo level kada smo dosli do izlaza
def restart_level():
	global level, w, h, exit_coords
	level = [1] * (w * h)
	for x in range(1, w, 2):
		for y in range(1, h, 2):
			maze.carve_maze(level, w, h, x, y)
	exit_coords = generate_exit(level, w, h)
	level[exit_coords[1] * w + exit_coords[0]] = 2
	player.x = 1
	player.y = 1


# uzimanje inputa od korisnika
def user_input():
	global running
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			running = False
		elif ev.type == pygame.KEYDOWN:
			if ev.key == pygame.K_q:
				running = False

	keys = pygame.key.get_pressed()

	# sve dok je odgovarajuce dugme pritisnuto pomeramo igraca
	# ako je blok na koji zelimo da ga pomerimo slobodan
	if keys[pygame.K_LEFT]:
		if level[player.y * w + player.x - 1] == 0:
			player.move(Player.PlayerDir.LEFT)
		elif level[player.y * w + player.x - 1] == 2:
			restart_level()
	if keys[pygame.K_RIGHT]:
		if level[player.y * w + player.x + 1] == 0:
			player.move(Player.PlayerDir.RIGHT)
		elif level[player.y * w + player.x + 1] == 2:
			restart_level()
	if keys[pygame.K_UP]:
		if level[(player.y - 1) * w + player.x] == 0:
			player.move(Player.PlayerDir.UP)
		elif level[(player.y - 1) * w + player.x] == 2:
			restart_level()
	if keys[pygame.K_DOWN]:
		if level[(player.y + 1) * w + player.x] == 0:
			player.move(Player.PlayerDir.DOWN)
		elif level[(player.y + 1) * w + player.x] == 2:
			restart_level()


# renderovanje tekstura na ekranu
def render():
	window.fill(grey)
	for x in range(0, w):
		for y in range(0, h):
			block = level[y * w + x]
			# u zavistnosti koji blok je trenutni blok koji se iscrtavamo
			# odgovarajucu teksturu
			size = env.BLOCK_SIZE[0]
			if block == 1:
				window.blit(wall_sprite, (x * size, y * size))
			elif block == 2:
				window.blit(exit_sprite, (x * size, y * size))

	# crtamo igraca poslednjeg i apdejtujemo ekran
	# bez update se nista ne prikazuje
	player.blit(window)
	pygame.display.update()


# implementacija logike igrice
# npr. enemy itd.
def update():
	pass


# proveravanje kolizije dva bloka
def check_collision(x1, y1, x2, y2, size):
	return x2 <= x1 < x2 + size and y2 <= y1 < y2 + size


# game loop
# 1 - uzimamo input od korisnika
# 2 - izvrsavamo logiku igrice
# 3 - iscrtavamo sve promene na ekran
while running:
	user_input()
	update()
	render()
	pygame.time.wait(fps)
