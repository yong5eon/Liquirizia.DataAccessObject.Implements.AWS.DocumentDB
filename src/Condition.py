# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

__all__ = (
	'Condition'
)


class Condition(metaclass=ABCMeta):
	"""Condition Interface of Filter for AWS DocumentDB"""

	@abstractmethod
	def __init__(self, *args, **kwargs):
		raise NotImplementedError('{} must be implemented __init__'.format(self.__class__.__name__))

	@abstractmethod
	def __call__(self):
		raise NotImplementedError('{} must be implemented __call__'.format(self.__class__.__name__))

	@abstractmethod
	@property
	def key(self):
		raise NotImplementedError('{} must be implemented key'.format(self.__class__.__name__))

	@abstractmethod
	@property
	def expression(self):
		raise NotImplementedError('{} must be implemented expression'.format(self.__class__.__name__))
