# -*- coding: utf-8 -*-

from ..Condition import Condition

__all__ = (
	'Or'
)


class Or(Condition):
	"""
	Data Access Object Filter Or Class for DocumentDB of AWS
	"""
	def __init__(self, conditions: list[Condition] = None):
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

	def add(self, condition: Condition):
		if not issubclass(condition.__class__, Condition):
			raise RuntimeError('{} must be derived from Condition'.format(condition.__class__.__name__))
		self.conditions.append(condition)
		return self

	def clear(self):
		self.conditions.clear()
		return self
