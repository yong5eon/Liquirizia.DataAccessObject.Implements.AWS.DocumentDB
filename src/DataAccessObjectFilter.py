# -*- coding: utf-8 -*-

from .DataAccessObjectFilterCondition import DataAccessObjectFilterCondition

__all__ = (
	'DataAccessObjectFilter'
)


class DataAccessObjectFilter(object):
	"""
	Data Access Object Filter Class for DocumentDB of AWS
	"""
	def __init__(self, conditions: [DataAccessObjectFilterCondition] = None):
		super(DataAccessObjectFilter, self).__init__()
		self.conditions = conditions if conditions else []
		for condition in self.conditions:
			if not issubclass(condition.__class__, DataAccessObjectFilterCondition):
				raise RuntimeError('{} must be derived from DataAccessObjectFilterCondition'.format(condition.__class__.__name__))
		return

	def __call__(self):
		f = {}
		for condition in self.conditions:
			if condition.key in f:
				f[condition.key].update(condition.expression)
			else:
				f[condition.key] = condition.expression
		return f

	def add(self, condition: DataAccessObjectFilterCondition):
		if not issubclass(condition.__class__, DataAccessObjectFilterCondition):
			raise RuntimeError('{} must be derived from DataAccessObjectFilterCondition'.format(condition.__class__.__name__))
		self.conditions.append(condition)
		return self

	def clear(self):
		self.conditions.clear()
		return self
