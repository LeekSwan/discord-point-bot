from connect import connection

cursor = connection()
cursor.execute('SELECT NOW()')
print(cursor.fetchall())


def get_all_user_points():
    cursor.execute("SELECT * FROM points")
    return cursor.fetchall()

def get_points_by_user_name(user_name):
    cursor.execute('SELECT * FROM points WHERE user_name = %s', user_name)
    # print(cursor.fetchall())
    return cursor.fetchall()

def add_points_to_user(user_name, points):
    # check if user exists. If not, add new user otherwise increment
    cursor.execute("UPDATE points SET points = points + %s WHERE user_name = %s", (points, user_name))

def remove_points_from_user(user_name, points):
    # check for negatives. Points should not go below 0
    cursor.execute("UPDATE points SET points = points - %s WHERE user_name = %s", (points, user_name))

def set_points(user_name, points):
    cursor.execute("UPDATE points SET points = %s WHERE user_name = %s", (points, user_name))
