# -*- coding: utf-8 -*-

from ..Condition import Condition

__all__ = (
	'Regex'
)


class Regex(Condition):
	"""
	Data Access Object Filter Regex Class for DocumentDB of AWS
	"""
	def __init__(self, key, pattern, options=None):
		self.k = key
		self.pattern = pattern
		self.options = options
		return

	def __call__(self):
		return {self.k: {'$regex': self.pattern}} if not self.options else {self.k: {'$regex': self.pattern, '$options': self.options}}

	@property
	def key(self):
		return self.k

	@property
	def expression(self):
		if self.options:
			return {'$regex': self.pattern, '$options': self.options}
		return {'$regex': self.pattern}
