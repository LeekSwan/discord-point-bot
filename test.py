from connect import connection

cursor = connection()
cursor.execute('SELECT NOW()')
print(cursor.fetchall())
