from enum import Enum
import env


class Player(object):
	class MoveDir(Enum):
		UP = 0
		DOWN = 1
		LEFT = 2
		RIGHT = 3

	def __init__(self, sprite, x=0, y=0) -> None:
		super().__init__()
		self.max_move = 2
		self.next_move = self.max_move
		self.x = x
		self.y = y
		self.sprite = sprite

	def blit(self, screen):
		screen.blit(self.sprite, (self.x * env.BLOCK_SIZE[0], self.y * env.BLOCK_SIZE[0]))

	def move(self, d: MoveDir):
		if self.next_move == 0:
			self.next_move = self.max_move
			if d == Player.MoveDir.DOWN:
				self.y += 1
			elif d == Player.MoveDir.UP:
				self.y -= 1
			elif d == Player.MoveDir.LEFT:
				self.x -= 1
			elif d == Player.MoveDir.RIGHT:
				self.x += 1
			else:
				raise AssertionError("Invalid argument")
		else:
			self.next_move -= 1
