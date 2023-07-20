# -*- coding: utf-8 -*-

from datetime import datetime, date
from decimal import Decimal

__all__ = (
	'DataAccessObjectFormatEncoder'
)


class DataAccessObjectFormatEncoder(object):
	def __call__(self, o):
		if isinstance(o, Decimal):
			return float(o)
		if isinstance(o, (date, datetime)):
			return o.isoformat()
		return o
