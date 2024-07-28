# -*- coding: utf-8 -*-

from ..Condition import Condition

__all__ = (
	'NotEqual'
)


class NotEqual(Condition):
	"""
	Data Access Object Filter Not Equal Class for DocumentDB of AWS
	"""
	def __init__(self, key, value):
		self.k = key
		self.v = value
		return

	def __call__(self):
		return {self.k: {'$ne': self.v}}

	@property
	def key(self):
		return self.k

	@property
	def expression(self):
		return {'$ne': self.v}
