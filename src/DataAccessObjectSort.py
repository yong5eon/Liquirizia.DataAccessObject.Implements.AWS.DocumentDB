# -*- coding: utf-8 -*-

from .DataAccessObjectSortKey import DataAccessObjectSortKey

__all__ = (
	'DataAccessObjectSort'
)


class DataAccessObjectSort(object):
	"""
	Data Access Object Sort Class for DocumentDB of AWS
	"""
	def __init__(self, keys=None):
		super(DataAccessObjectSort, self).__init__()
		if keys is None:
			keys = []
		if isinstance(keys, DataAccessObjectSortKey):
			keys = [keys]
		if not isinstance(keys, (list, tuple)):
			raise RuntimeError('{} is not iterable'.format(keys.__class__.__name__))
		self.keys = list()
		for key in keys:
			if not isinstance(key, DataAccessObjectSortKey):
				raise RuntimeError('{} must be DataAccessObjectSortKey or list of DataAccessObjectSortKey'.format(key.__class__.__name__))
			self.keys.append(key)
		return

	def add(self, key, type):
		self.keys.append(DataAccessObjectSortKey(key, type))
		return self

	def clear(self):
		self.keys.clear()
		return self
