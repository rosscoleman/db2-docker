from sqlalchemy import *

# Fails in ibm_db_sa 0.3.4 because 'future' module doesn't exist in Python  https://github.com/ibmdb/python-ibmdbsa/issues/46
# Fix: https://github.com/ibmdb/python-ibmdbsa/commit/220029fd7455c62b69dadd3c3d60744c11b76ccb
# Can be fixed by pip install future
db2 = create_engine("db2+ibm_db://db2inst1:password@localhost:60000/testdb")

metadata = MetaData()

users = Table('STAFF', metadata, 
Column('ID', Integer, primary_key = True),
Column('NAME', String(9), nullable = False),
Column('DEPT', Integer, nullable = False),
Column('JOB', String(5), nullable = False)
)