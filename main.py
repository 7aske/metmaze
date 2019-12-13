import pygame
import spritesheet

pygame.init()

window_size = (1024, 768)

window = pygame.display.set_mode(window_size)

grey = (34, 34, 34)

running = True

fps = 1000 // 69

sheet = spritesheet.Spritesheet()

player_sprite = sheet.sprite_at(4, 8)
player_pos=[0,0]

# CTRL ALT L


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
		player_pos[0] -= 1
		print("Left pressed")
	if keys[pygame.K_RIGHT]:
		player_pos[0] += 1
		print("Right pressed")
	if keys[pygame.K_UP]:
		player_pos[1] -= 1
		print("Up pressed")
	if keys[pygame.K_DOWN]:
		player_pos[1] += 1
		print("Down pressed")


def render():
	window.fill(grey)

	window.blit(player_sprite, (player_pos[0], player_pos[1]))
	pygame.display.update()


def update():
	pass


while running:
	user_input()
	update()
	render()
	pygame.time.wait(fps)
