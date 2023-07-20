# -*- coding: utf-8 -*-

from ..DataAccessObjectFilterCondition import DataAccessObjectFilterCondition

__all__ = (
	'DataAccessObjectFilterLessThan'
)


class DataAccessObjectFilterLessThan(DataAccessObjectFilterCondition):
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
