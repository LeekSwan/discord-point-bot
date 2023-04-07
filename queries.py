from connect import connection

cursor = connection()
cursor.execute('SELECT NOW()')
print(cursor.fetchall())


def get_points_by_user_name(user_name):
    cursor.execute('SELECT * FROM points WHERE user_name = %s', user_name)
    print(cursor.fetchall())