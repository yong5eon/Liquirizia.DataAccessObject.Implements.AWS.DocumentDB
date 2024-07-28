# -*- coding: utf-8 -*-

from ..Condition import Condition

__all__ = (
	'Exists'
)


class Exists(Condition):
	"""
	Data Access Object Filter Exists Class for DocumentDB of AWS
	"""
	def __init__(self, key, value):
		self.k = key
		self.v = value
		return

	def __call__(self):
		return {self.k: {'$exists': self.v}}

	@property
	def key(self):
		return self.k

	@property
	def expression(self):
		return {'$exists': self.v}
