# Liquirizia.DataAccessObject.Implements.AWS.DocumentDB
AWS DocumentDB Data Access Object for Liquirizia

## 사용 방법
```python
# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import DataAccessObjectHelper  # 헬퍼 임포트

from Liquirizia.DataAccessObject.Implements.AWS.DocumentDB import DataAccessObject, DataAccessObjectConfiguration
from Liquirizia.DataAccessObject.Implements.AWS.DocumentDB import DataAccessObjectIndexes, DataAccessObjectIndex, DataAccessObjectIndexKey
from Liquirizia.DataAccessObject.Implements.AWS.DocumentDB import DataAccessObjectSort, DataAccessObjectSortKey, DataAccessObjectFilter
from Liquirizia.DataAccessObject.Implements.AWS.DocumentDB.Filters import (
	DataAccessObjectFilterGreaterThan,
	DataAccessObjectFilterLessThan,
	DataAccessObjectFilterIn,
	DataAccessObjectFilterNotIn,
	DataAccessObjectFilterEqual,
	DataAccessObjectFilterNotEqual,
)

if __name__ == '__main__':
	# Set connection
	DataAccessObjectHelper.Set(
		'Sample',
		DataAccessObject,
		DataAccessObjectConfiguration(
			host='HOST_ADDRESS',
			port=27017,
			username='USER_NAME',
			password='PASSWORD',
			database='DATABASE',
			tls=True,
			ca='Sample.pem'
		)
	)

	# Get connection
	con = DataAccessObjectHelper.Get('Sample')

	# create document table
	con.create(
		'Sample',
		DataAccessObjectIndexes([
			DataAccessObjectIndex(DataAccessObjectIndexKey('ID', DataAccessObjectIndexKey.ASCENDING), unique=True),
			DataAccessObjectIndex(DataAccessObjectIndexKey('Name', DataAccessObjectIndexKey.ASCENDING), unique=True),
			# DataAccessObjectIndex(DataAccessObjectIndexKey('CountryCode', DataAccessObjectIndexKey.TEXT)),
		])
	)

	# set document
	con.set(
		'Sample',
		id=1,
		doc={
			'ID': 1,
			'Name': '최준호',
			'CountryCode': 'KR',
			'Dept': '연구소',
			'Title': '개발'
		}
	)

	con.set(
		'Sample',
		id=2,
		doc={
			'ID': 2,
			'Name': '홍승걸',
			'CountryCode': 'KR',
			'Dept': '연구소',
			'Title': '개발'
		}
	)

	con.set(
		'Sample',
		id=3,
		doc={
			'ID': 3,
			'Name': '허용선',
			'CountryCode': 'KR',
			'Title': 'CTO'
		}
	)
	print(con.total('Sample'))

	# get document
	doc = con.get(
		'Sample',
		id=1
	)
	print(doc)

	docs = con.query(
		'Sample',
		filter=DataAccessObjectFilter((
			DataAccessObjectFilterEqual('CountryCode', 'KR'),
			DataAccessObjectFilterNotEqual('Title', 'CTO'),
		)),
		sort=DataAccessObjectSort(DataAccessObjectSortKey('Name', DataAccessObjectSortKey.ASCENDING)),
		limit=3
	)
	print(docs)

	docs = con.query(
		'Sample',
		filter=DataAccessObjectFilter((
			DataAccessObjectFilterGreaterThan('ID', 1),
			DataAccessObjectFilterLessThan('ID', 4),
		)),
		sort=DataAccessObjectSort(DataAccessObjectSortKey('Name', DataAccessObjectSortKey.ASCENDING)),
		limit=2
	)
	print(docs)

	docs = con.query(
		'Sample',
		filter=DataAccessObjectFilter((
			DataAccessObjectFilterIn('ID', 1),
		)),
		sort=DataAccessObjectSort(DataAccessObjectSortKey('Name', DataAccessObjectSortKey.ASCENDING)),
		limit=3
	)
	print(docs)

	docs = con.query(
		'Sample',
		filter=DataAccessObjectFilter((
			DataAccessObjectFilterIn('ID', (1, 2, 3)),
			DataAccessObjectFilterNotIn('ID', 1),
		)),
		sort=DataAccessObjectSort(DataAccessObjectSortKey('Name', DataAccessObjectSortKey.ASCENDING)),
		limit=3
	)
	print(docs)

	# delete document
	con.remove(
		'Sample',
		id=1
	)

	# delete document table
	con.delete('Sample')

	con.close()
	del con
```