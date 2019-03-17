import ibm_db_dbi as db

#conn = ibm_db.connect('testdb', 'db2inst1', 'password')

conn_dsn = "DATABASE=testdb;HOSTNAME=localhost;PORT=60000;PROTOCOL=TCPIP;UID=db2inst1;PWD=password;"

conn = db.connect(conn_dsn, "", "")
cursor = conn.cursor()
cursor.execute("select * from syscat.tables where type = 'T'")
for r in cursor.fetchall():
    print(r)

