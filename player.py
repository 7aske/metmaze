import env
from enum import Enum

class Player:
	class PlayerDir(Enum):
		UP=0
		DOWN=1
		LEFT=2
		RIGHT=3

	# konstruktor i njegova tri parametra
	# self postoji u svako metodi u klasi (slef = this u C#)
	def __init__(self, sprite, x=1, y=1):
		self.x = x
		self.y = y
		self.sprite = sprite
		self.max_move = 2
		self.next_move = self.max_move

	# pomocna metoda za iscrtavanje samog igracana ekranu
	def blit(self, screen):
		screen.blit(self.sprite, (self.x * env.BLOCK_SIZE[0], self.y * env.BLOCK_SIZE[1]))

	# pomeramo igraca u zavisnosti od toga da li smo sacekali dovoljno od
	# prethodnog trenutka kada samo se pomerili
	def move(self, d: PlayerDir):
		if self.next_move == 0:
			self.next_move = self.max_move
			if d == Player.PlayerDir.UP:
				self.y -= 1
			elif d == Player.PlayerDir.DOWN:
				self.y += 1
			elif d == Player.PlayerDir.LEFT:
				self.x -= 1
			elif d == Player.PlayerDir.RIGHT:
				self.x += 1
		else:
			self.next_move -= 1