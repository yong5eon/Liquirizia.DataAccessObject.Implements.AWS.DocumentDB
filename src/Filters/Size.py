# -*- coding: utf-8 -*-

from ..Condition import Condition

__all__ = (
	'Size'
)


class Size(Condition):
	"""
	Data Access Object Filter Size Class for DocumentDB of AWS
	"""
	def __init__(self, key, size):
		self.k = key
		self.size = size
		return

	def __call__(self):
		return {self.k: {'$size': self.size}}

	@property
	def key(self):
		return self.k

	@property
	def expression(self):
		return {'$size': self.size}
