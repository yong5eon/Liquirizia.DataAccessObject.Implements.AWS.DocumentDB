# -*- coding: utf-8 -*-

from Liquirizia.DataAccessObject import Helper

from Liquirizia.DataAccessObject.Implements.AWS.DocumentDB import Connection, Configuration
from Liquirizia.DataAccessObject.Implements.AWS.DocumentDB import Indexes, Index, IndexKey
from Liquirizia.DataAccessObject.Implements.AWS.DocumentDB import Sort, SortKey, Filter
from Liquirizia.DataAccessObject.Implements.AWS.DocumentDB.Filters import * 

if __name__ == '__main__':
	# Set connection
	Helper.Set(
		'Sample',
		Connection,
		Configuration(
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
	con = Helper.Get('Sample')

	# con.delete('Sample')
	# time.sleep(3)

	# create document table
	con.delete('Sample')
	con.create(
		'Sample',
		Indexes([
			Index(IndexKey('ID', IndexKey.ASCENDING), unique=True),
			Index(IndexKey('Name', IndexKey.ASCENDING), unique=True),
			# Index(IndexKey('CountryCode', IndexKey.TEXT)),
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
			'Title': '개발자'
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
			'Title': '개발자'
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
		filter=Filter((
			Equal('CountryCode', 'KR'),
			NotEqual('Title', 'CTO'),
		)),
		sort=Sort(SortKey('Name', SortKey.ASCENDING)),
		limit=3
	)
	print(docs)

	docs = con.query(
		'Sample',
		filter=Filter((
			GreaterThan('ID', 1),
			LessThan('ID', 4),
		)),
		sort=Sort(SortKey('Name', SortKey.ASCENDING)),
		limit=2
	)
	print(docs)

	docs = con.query(
		'Sample',
		filter=Filter((
			In('ID', 1),
		)),
		sort=Sort(SortKey('Name', SortKey.ASCENDING)),
		limit=3
	)
	print(docs)

	docs = con.query(
		'Sample',
		filter=Filter((
			In('ID', (1, 2, 3)),
			NotIn('ID', 1),
		)),
		sort=Sort(SortKey('Name', SortKey.ASCENDING)),
		limit=3
	)
	print(docs)

	# delete document
	con.remove(
		'Sample',
		id=1
	)

# delete document table
# con.delete('Sample')

	con.close()
	del con
