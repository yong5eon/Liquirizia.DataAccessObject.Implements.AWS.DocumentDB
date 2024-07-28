# -*- coding: utf-8 -*-

from ..Condition import Condition

__all__ = (
	'LessThan'
)


class LessThan(Condition):
	"""
	Data Access Object Filter Less Than Class for DocumentDB of AWS
	"""
	def __init__(self, key, value):
		self.k = key
		self.v = value
		return

	def __call__(self):
		return {self.k: {'$lt': self.v}}

	@property
	def key(self):
		return self.k

	@property
	def expression(self):
		return {'$lt': self.v}
