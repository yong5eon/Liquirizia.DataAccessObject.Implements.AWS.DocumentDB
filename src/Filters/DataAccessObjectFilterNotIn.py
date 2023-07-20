# -*- coding: utf-8 -*-

from ..DataAccessObjectFilterCondition import DataAccessObjectFilterCondition

__all__ = (
	'DataAccessObjectFilterNotIn'
)


class DataAccessObjectFilterNotIn(DataAccessObjectFilterCondition):
	"""
	Data Access Object Filter Not In Class for DocumentDB of AWS
	"""
	def __init__(self, key, values):
		self.k = key
		self.v = values if isinstance(values, (list, tuple)) else [values]
		return

	def __call__(self):
		return {self.k: {'$nin': self.v}}

	@property
	def key(self):
		return self.k

	@property
	def expression(self):
		return {'$nin': self.v}
