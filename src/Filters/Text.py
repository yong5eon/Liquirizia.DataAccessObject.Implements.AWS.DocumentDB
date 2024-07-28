# -*- coding: utf-8 -*-

from ..Condition import Condition

__all__ = (
	'Text'
)


class Text(Condition):
	"""
	Data Access Object Filter Text Class for DocumentDB of AWS
	"""
	def __init__(self, key, search: str, lang:str = None, case: bool = None, diacritic: bool = None):
		self.k = key
		self.search = search
		self.lang = lang
		self.case = case
		self.diacritic = diacritic
		return

	def __call__(self):
		# TODO : return pattern to filter using text
		pass

	@property
	def key(self):
		return self.k

	@property
	def expression(self):
		params = {
			'$search': self.search
		}
		if self.lang:
			params['$language'] = self.lang
		if self.case:
			params['$caseSensitive'] = self.case
		if self.diacritic:
			params['$diacriticSensitive'] = self.diacritic
		return {'$text': params}
