# -*- coding: utf-8 -*-

from .DataAccessObjectIndexKey import DataAccessObjectIndexKey

__all__ = (
	'DataAccessObjectIndex'
)


class DataAccessObjectIndex(object):
	"""
	Data Access Object Index Class for DocumentDB of AWS
	"""
	def __init__(self, keys=None, unique=False, sparse=False, background=True, expires=None):
		super(DataAccessObjectIndex, self).__init__()
		if keys is None:
			keys = []
		if isinstance(keys, DataAccessObjectIndexKey):
			keys = [keys]
		if not isinstance(keys, (list, tuple)):
			raise RuntimeError('{} is not iterable'.format(keys.__class__.__name__))
		self.keys = list()
		for key in keys:
			if not isinstance(key, DataAccessObjectIndexKey):
				raise RuntimeError('{} must be DataAccessObjectIndexKey or list of DataAccessObjectIndexKey'.format(key.__class__.__name__))
			self.keys.append(key)
		self.properties = dict(
			unique=unique,
			sparse=sparse,
			background=background,
			expires=expires,
		)
		return

	def add(self, key, type):
		self.keys.append(DataAccessObjectIndexKey(key, type))
		return self

	def clear(self):
		self.keys.clear()
		return self

	@property
	def unique(self):
		return self.properties['unique']

	@unique.setter
	def setUnique(self, v: bool):
		self.properties['unique'] = v
		return

	@property
	def sparse(self):
		return self.properties['sparse']

	@sparse.setter
	def setSparse(self, v: bool):
		self.properties['sparse'] = v
		return

	@property
	def background(self):
		return self.properties['background']

	@background.setter
	def setBackground(self, v: bool):
		self.properties['background'] = v
		return

	@property
	def expires(self):
		return self.properties['expires']

	@expires.setter
	def setExpires(self, v: int):
		self.properties['expires'] = v
		return
