# -*- coding: utf-8 -*-

from .Condition import Condition

__all__ = (
	'Filter'
)


class Filter(object):
	"""Filter Class for AWS DocumentDB"""

	def __init__(self, conditions: list[Condition] = None):
		super(Filter, self).__init__()
		self.conditions = conditions if conditions else []
		for condition in self.conditions:
			if not issubclass(condition.__class__, Condition):
				raise RuntimeError('{} must be derived from FilterCondition'.format(condition.__class__.__name__))
		return

	def __call__(self):
		f = {}
		for condition in self.conditions:
			if condition.key in f:
				f[condition.key].update(condition.expression)
			else:
				f[condition.key] = condition.expression
		return f

	def add(self, condition: Condition):
		if not issubclass(condition.__class__, Condition):
			raise RuntimeError('{} must be derived from FilterCondition'.format(condition.__class__.__name__))
		self.conditions.append(condition)
		return self

	def clear(self):
		self.conditions.clear()
		return self
