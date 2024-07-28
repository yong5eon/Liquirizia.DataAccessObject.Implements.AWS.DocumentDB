# -*- coding: utf-8 -*-

from ..Condition import Condition

__all__ = (
	'Mod'
)


class Mod(Condition):
	"""
	Data Access Object Filter Modulo Class for DocumentDB of AWS
	"""
	def __init__(self, key, div: int, expr: int):
		self.k = key
		self.div = div
		self.expr = expr
		return

	def __call__(self):
		return {self.k: {'$mod': [self.div, self.expr]}}

	@property
	def key(self):
		return self.k

	@property
	def expression(self):
		return {'$mod': [self.div, self.expr]}
