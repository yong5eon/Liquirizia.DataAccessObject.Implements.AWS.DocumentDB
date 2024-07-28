# -*- coding: utf-8 -*-

from pymongo import ASCENDING, DESCENDING, GEO2D, GEOSPHERE, HASHED, TEXT

__all__ = (
	'IndexKey'
)


class IndexKey(object):
	"""Index Key Class for AWS DocumentDB"""

	ASCENDING = ASCENDING
	DESCENDING = DESCENDING
	GEO2D = GEO2D
	GEOSPHERE = GEOSPHERE
	HASH = HASHED
	TEXT = TEXT

	def __init__(self, key=None, type=None):
		super(IndexKey, self).__init__()
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
