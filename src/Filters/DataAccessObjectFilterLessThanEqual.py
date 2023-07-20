# -*- coding: utf-8 -*-

from ..DataAccessObjectFilterCondition import DataAccessObjectFilterCondition

__all__ = (
	'DataAccessObjectFilterLessThanEqual'
)


class DataAccessObjectFilterLessThanEqual(DataAccessObjectFilterCondition):
	"""
	Data Access Object Filter Less Than Equal Class for DocumentDB of AWS
	"""
	def __init__(self, key, value):
		self.k = key
		self.v = value
		return

	def __call__(self):
		return {self.k: {'$lte': self.v}}

	@property
	def key(self):
		return self.k

	@property
	def expression(self):
		return {'$lte': self.v}
