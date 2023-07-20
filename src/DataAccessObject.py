# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import DataAccessObject as DataAccessObjectBase
from Liquirizia.DataAccessObject.Properties.Document import Document

from Liquirizia.DataAccessObject import DataAccessObjectError
from Liquirizia.DataAccessObject.Errors import *

from .DataAccessObjectConfiguration import DataAccessObjectConfiguration
from .DataAccessObjectIndexes import DataAccessObjectIndexes
from .DataAccessObjectSort import DataAccessObjectSort
from .DataAccessObjectFilter import DataAccessObjectFilter

from .DataAccessObjectFormatEncoder import DataAccessObjectFormatEncoder
from .DataAccessObjectFormatDecoder import DataAccessObjectFormatDecoder

from Liquirizia.Util.Dictionary import Replace

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection
from pymongo.errors import ConnectionFailure

from bson.objectid import ObjectId
from hashlib import shake_256

__all__ = (
	'DataAccessObject'
)


class DataAccessObject(DataAccessObjectBase, Document):
	"""
	Data Access Object Class for DocumentDB of AWS

	TODO :
		* Exception Handling with DataAccessObjectError
	"""

	def __init__(self, conf: DataAccessObjectConfiguration, decoder=DataAccessObjectFormatDecoder(), encoder=DataAccessObjectFormatEncoder()):
		self.conf = conf
		self.connection = None
		self.database = None
		self.decoder = decoder
		self.encoder = encoder
		return

	def __del__(self):
		self.close()
		return

	def __id__(self, id):
		hash = shake_256()
		hash.update(str(id).encode('utf-8'))
		return ObjectId(hash.digest(12))

	def connect(self):
		try:
			self.connection = MongoClient(
				host=self.conf.host,
				port=self.conf.port,
				username=self.conf.username,
				password=self.conf.password,
				tls=self.conf.tls,
				tlsCAFile=self.conf.ca,
				retryWrites=self.conf.retryWrites,
				replicaSet=self.conf.replicaSet,
				readPreference=self.conf.readPreference,
				directConnection=self.conf.directConnection,
			)
			self.database = Database(self.connection, self.conf.database)
		except ConnectionFailure as e:
			raise DataAccessObjectConnectionError(error=e)
		return

	def close(self):
		if self.connection:
			self.connection.close()
			self.connection = None
			self.database = None
		return

	def create(self, key: str, indexes: DataAccessObjectIndexes = None):
		keys = self.database.list_collection_names()
		if key in keys:
			raise DataAccessObjectError('{} is exists'.format(key))
		document = Collection(self.database, key)
		for index in indexes if indexes else []:
			keys = []
			for key in index.keys:
				keys.append((key.key, key.type))
			params = dict(
				unique=index.unique,
				background=index.background,
			)
			if index.sparse:
				params['sparse'] = index.sparse
			if index.expires:
				params['expireAfterSeconds'] = index.expires
			document.create_index(keys, **params)
		return document

	def set(self, key: str, id, doc):
		if not isinstance(doc, dict):
			raise RuntimeError('{} is not mutable mapping(dict)'.format(doc.__class__.__name__))
		document = Collection(self.database, key)
		return document.replace_one({'_id': self.__id__(id)}, Replace(doc, self.encoder), upsert=True)

	def get(self, key: str, id):
		document = Collection(self.database, key)
		doc = document.find_one({'_id': self.__id__(id)})
		if not doc:
			return None
		del doc['_id']
		return Replace(doc, self.decoder)

	def remove(self, key, id):
		document = Collection(self.database, key)
		return document.delete_one({'_id': self.__id__(id)})
	
	def query(self, key, filter: DataAccessObjectFilter = None, sort: DataAccessObjectSort = None, limit=None, pos=None, projection: tuple[str] = None, timeout=None):
		document = Collection(self.database, key)
		s = []
		for key in sort.keys if sort else []:
			s.append((key.key, key.type))
		cursor = document.find(
			filter=filter() if filter else {},
			sort=s,
			limit=limit if limit else 0,
			skip=pos if pos else 0,
			projection=projection,
		)
		if timeout:
			cursor.max_time_ms(timeout)
		li = list()
		for i, c in enumerate(cursor):
			doc = Replace(c, self.decoder)
			del doc['_id']
			li.append(doc)
		return li if len(li) > 0 else None

	def delete(self, key):
		self.database.drop_collection(key)
		return

	def total(self, key):
		document = Collection(self.database, key)
		return document.count_documents({})
	
	def count(self, key, filter: DataAccessObjectFilter = None):
		document = Collection(self.database, key)
		return document.count_documents(filter() if filter else {})
