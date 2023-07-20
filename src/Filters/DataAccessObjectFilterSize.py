# -*- coding: utf-8 -*-

from ..DataAccessObjectFilterCondition import DataAccessObjectFilterCondition

__all__ = (
	'DataAccessObjectFilterSize'
)


class DataAccessObjectFilterSize(DataAccessObjectFilterCondition):
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
