import random


def generate_maze(w, h):
	m = [1] * (h * w)

	for y in range(1, h, 2):
		for x in range(1, w, 2):
			carve_maze(m, w, h, x, y)
	return m


def carve_maze(maze, w, h, x, y):
	# x1 = 0
	# y1 = 0
	# x2 = 0
	# y2 = 0
	# dx = 0
	# dy = 0
	# d = 0
	# count = 0

	d = random.randint(0, 3)
	count = 0
	while count < 4:
		dx = 0
		dy = 0
		if d == 0:
			dx = 1
		elif d == 1:
			dy = 1
		elif d == 2:
			dx = -1
		else:
			dy = -1
		x1 = x + dx
		y1 = y + dy
		x2 = x1 + dx
		y2 = y1 + dy

		if 0 < x2 < w - 1 and \
				0 < y2 < h - 1 and \
				maze[y1 * w + x1] == 1 and \
				maze[y2 * w + x2] == 1:
			maze[y1 * w + x1] = 0
			maze[y2 * w + x2] = 0
			x = x2
			y = y2
			d = random.randint(0, 3)
			count = 0
		else:
			d = (d + 1) % 4
			count += 1


