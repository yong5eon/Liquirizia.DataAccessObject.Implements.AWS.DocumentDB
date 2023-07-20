# -*- coding: utf-8 -*-

from ..DataAccessObjectFilterCondition import DataAccessObjectFilterCondition

__all__ = (
	'DataAccessObjectFilterOr'
)


class DataAccessObjectFilterOr(DataAccessObjectFilterCondition):
	"""
	Data Access Object Filter Or Class for DocumentDB of AWS
	"""
	def __init__(self, conditions: list[DataAccessObjectFilterCondition] = None):
		self.conditions = conditions if conditions else []
		return

	def __call__(self):
		expr = {
			'$or': []
		}
		for condition in self.conditions:
			expr['$or'].append(condition())
		return expr

	@property
	def key(self):
		return '$or'

	@property
	def expression(self):
		expr = []
		for condition in self.conditions:
			expr.append(condition())
		return expr

	def add(self, condition: DataAccessObjectFilterCondition):
		if not issubclass(condition.__class__, DataAccessObjectFilterCondition):
			raise RuntimeError('{} must be derived from DataAccessObjectFilterCondition'.format(condition.__class__.__name__))
		self.conditions.append(condition)
		return self

	def clear(self):
		self.conditions.clear()
		return self
