# -*- coding: utf-8 -*-

from pymongo import ASCENDING, DESCENDING

__all__ = (
	'SortKey'
)


class SortKey(object):
	"""
	Data Access Object Sort Key Class for DocumentDB of AWS
	"""

	ASCENDING = ASCENDING
	DESCENDING = DESCENDING

	def __init__(self, key=None, type=None):
		super(SortKey, self).__init__()
		self.properties = dict(
			key=key,
			type=type,
		)
		return

	@property
	def key(self):
		return self.properties['key']

	@key.setter
	def setKey(self, v):
		self.properties['key'] = v
		return

	@property
	def type(self):
		return self.properties['type']

	@type.setter
	def setType(self, v):
		self.properties['type'] = v
		return
