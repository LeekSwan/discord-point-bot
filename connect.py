import time
import os
from psycopg2.extensions import connection
from psycopg2.pool import SimpleConnectionPool
from dotenv import load_dotenv

load_dotenv()
connect = cursor = db = None

conn_string = os.environ.get('DB_CONNECT')
min_conn = 0
max_conn = 100

# if __name__ == '__main__':
#     # instantiate a connection pool
#     pool = SimpleConnectionPool(min_conn, max_conn, conn_string)
#
#     # fetch a connection from the pool. if no existing live connection exists,
#     # then a new one will be instantiated.
#     conn: connection = pool.getconn()
#     # run some query using the connection
#     with conn.cursor() as cur:
#         cur.execute('SELECT * FROM points')
#         print(cur.fetchall())
#
#     # return the connection to the pool to free it up for reuse. not that we
#     # could also add the keywork argument close=True here if we wanted to close
#     # the connection as soon as it is returned from the pool.
#     pool.putconn(conn)



def connection():
    pool = SimpleConnectionPool(min_conn, max_conn, conn_string)
    conn: connection = pool.getconn()
    cursor = conn.cursor()
    return cursor


# cursor = connection()
# cursor.execute('SELECT NOW()')
# print(cursor.fetchall())