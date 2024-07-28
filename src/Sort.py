# -*- coding: utf-8 -*-

from .SortKey import SortKey

__all__ = (
	'Sort'
)


class Sort(object):
	"""Sort Class for AWS DocumentDB"""

	def __init__(self, keys=None):
		super(Sort, self).__init__()
		if keys is None:
			keys = []
		if isinstance(keys, SortKey):
			keys = [keys]
		if not isinstance(keys, (list, tuple)):
			raise RuntimeError('{} is not iterable'.format(keys.__class__.__name__))
		self.keys = list()
		for key in keys:
			if not isinstance(key, SortKey):
				raise RuntimeError('{} must be SortKey or list of SortKey'.format(key.__class__.__name__))
			self.keys.append(key)
		return

	def add(self, key, type):
		self.keys.append(SortKey(key, type))
		return self

	def clear(self):
		self.keys.clear()
		return self
