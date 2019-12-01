class Player(object):
	def __init__(self, sprite, x=0, y=0) -> None:
		super().__init__()
		self.x = x
		self.y = y
		self.sprite = sprite

	def blit(self, screen):
		screen.blit(self.sprite, (self.x, self.y))
