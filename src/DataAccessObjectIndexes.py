# -*- coding: utf-8 -*-

from .DataAccessObjectIndex import DataAccessObjectIndex

from collections import MutableSequence

__all__ = (
	'DataAccessObjectIndex'
)


class DataAccessObjectIndexes(MutableSequence):
	"""
	Data Access Object Index Class for DocumentDB of AWS
	"""

	def __init__(self, indexes=None, unique=None, sparse=None, background=None, expires=None):
		super(DataAccessObjectIndexes, self).__init__()
		self.indexes = indexes if indexes else []
		self.properties = dict(
			unique=unique,
			sparse=sparse,
			background=background,
			expires=expires,
		)
		return

	def __getitem__(self, index):
		index = self.indexes[index]
		for k, v in self.properties.items():
			if v is not None:
				index.__setattr__(k, v)
		return index

	def __setitem__(self, index, value):
		self.indexes[index] = value
		return

	def __delitem__(self, index):
		del self.indexes[index]
		return

	def __len__(self):
		return len(self.indexes)

	def insert(self, index, value):
		self.indexes[index] = value
		return self

	def add(self, index: DataAccessObjectIndex):
		self.indexes.append(index)
		return self

	def clear(self):
		self.indexes.clear()
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
	def size(self):
		return self.properties['size']

	@size.setter
	def setSize(self, v: int):
		self.properties['size'] = v
		return

	@property
	def min(self):
		return self.properties['min']

	@min.setter
	def setMin(self, v: int):
		self.properties['min'] = v
		return

	@property
	def max(self):
		return self.properties['max']

	@max.setter
	def setMax(self, v: int):
		self.properties['max'] = v
		return

	@property
	def expires(self):
		return self.properties['expires']

	@expires.setter
	def setExpires(self, v: int):
		self.properties['expires'] = v
		return

	@property
	def expression(self):
		return self.properties['expression']

	@expression.setter
	def setExpression(self, v):
		self.properties['expression'] = v
		return

	@property
	def collation(self):
		return self.properties['collation']

	@collation.setter
	def setCollation(self, v):
		self.properties['collation'] = v
		return
