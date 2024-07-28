# -*- coding: utf-8 -*-

from ..Condition import Condition

__all__ = (
	'In'
)


class In(Condition):
	"""
	Data Access Object Filter In Class for DocumentDB of AWS
	"""
	def __init__(self, key, values):
		self.k = key
		self.v = values if isinstance(values, (list, tuple)) else [values]
		return

	def __call__(self):
		return {self.k: {'$in': self.v}}

	@property
	def key(self):
		return self.k

	@property
	def expression(self):
		return {'$in': self.v}
