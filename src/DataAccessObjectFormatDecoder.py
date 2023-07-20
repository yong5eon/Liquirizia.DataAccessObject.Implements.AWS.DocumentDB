# -*- coding: utf-8 -*-

from datetime import datetime, date

__all__ = (
	'DataAccessObjectFormatDecoder'
)


class DataAccessObjectFormatDecoder(object):
	def __call__(self, o):
		if isinstance(o, str):
			try:
				return date.fromisoformat(o)
			except:
				pass
			try:
				return datetime.fromisoformat(o)
			except:
				pass
		return o
