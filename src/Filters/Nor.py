# -*- coding: utf-8 -*-

from ..Condition import Condition

__all__ = (
	'Nor'
)


class Nor(Condition):
	"""
	Data Access Object Filter Nor Class for DocumentDB of AWS
	"""
	def __init__(self, conditions: list[Condition] = None):
		self.conditions = conditions if conditions else []
		return

	def __call__(self):
		expr = {
			'$nor': []
		}
		for condition in self.conditions:
			expr['$nor'].append(condition())
		return expr

	@property
	def key(self):
		return '$nor'

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
