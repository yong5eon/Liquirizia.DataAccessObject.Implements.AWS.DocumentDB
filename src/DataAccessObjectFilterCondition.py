# -*- coding: utf-8 -*-

__all__ = (
	'DataAccessObjectFilterCondition'
)


class DataAccessObjectFilterCondition(object):
	"""
	Data Access Object Filter Condition Interface Class for DocumentDB of AWS
	"""
	def __init__(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented __init__'.format(self.__class__.__name__))

	def __call__(self):
		raise NotImplementedError('{} must be implemented __call__'.format(self.__class__.__name__))

	@property
	def key(self):
		raise NotImplementedError('{} must be implemented key'.format(self.__class__.__name__))

	@property
	def expression(self):
		raise NotImplementedError('{} must be implemented expression'.format(self.__class__.__name__))
