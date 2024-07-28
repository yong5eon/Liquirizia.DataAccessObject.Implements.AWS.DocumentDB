# -*- coding: utf-8 -*-

from ..Condition import Condition

__all__ = (
	'All'
)


class All(Condition):
	"""
	Data Access Object Filter All Class for DocumentDB of AWS
	"""
	def __init__(self, key, values):
		self.k = key
		self.v = values
		return

	def __call__(self):
		return {self.k: {'$all': self.v}}

	@property
	def key(self):
		return self.k

	@property
	def expression(self):
		return {'$all': self.v}
