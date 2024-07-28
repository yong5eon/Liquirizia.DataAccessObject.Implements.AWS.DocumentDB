# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import Configuration as BaseConfiguration

__all__ = (
	'Configuration'
)


class Configuration(BaseConfiguration):
	"""Configuration Class for AWS DocumentDB"""

	def __init__(
		self,
		host,
		port,
		username,
		password,
		database,
		tls=False,
		ca=None,
		retryWrites=False,
		replicaSet='rs0',
		readPreference='secondaryPreferred',
		directConnection=False,
	):
		self.host = host
		self.port = port
		self.username = username
		self.password = password
		self.database = database
		self.tls = tls
		self.ca = ca
		self.retryWrites = retryWrites
		self.replicaSet = replicaSet if not directConnection else None
		self.readPreference = readPreference if not directConnection else 'primary'
		self.directConnection = directConnection
		return
