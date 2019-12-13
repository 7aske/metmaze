from enum import Enum

import pygame
import env

class Player:
	class PlayerDir(Enum):
		UP=0
		DOWN=1
		LEFT=2
		RIGHT=3

	def __init__(self, sprite, x=1, y=1):
		self.x = x
		self.y = y
		self.sprite = sprite
		self.max_move = 2
		self.next_move = self.max_move

	def blit(self, screen):
		screen.blit(self.sprite, (self.x * env.BLOCK_SIZE[0], self.y * env.BLOCK_SIZE[1]))

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