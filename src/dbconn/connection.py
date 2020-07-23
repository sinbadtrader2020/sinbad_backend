from psycopg2.pool import ThreadedConnectionPool
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager


class Connection:
    def __init__(self,
                 db_name=None,
                 db_username=None,
                 db_password=None,
                 db_hostname=None,
                 db_port=None):
        self.pool = ThreadedConnectionPool(1, 20,
                                           database=db_name,
                                           user=db_username,
                                           password=db_password,
                                           host=db_hostname,
                                           port=db_port)

    @contextmanager
    def get_db_connection(self):
        db_connection = None
        try:
            db_connection = self.pool.getconn()
            yield db_connection
        finally:
            self.pool.putconn(db_connection)

    @contextmanager
    def get_db_cursor(self, commit=False):
        with self.get_db_connection() as connection:
            cursor = connection.cursor(
                cursor_factory=RealDictCursor)
            try:
                yield cursor
                if commit:
                    connection.commit()
            finally:
                cursor.close()


db_config = {
    'db_name': 'halaltrading',
    'db_username': 'halaltrading',
    'db_password': '12345678',
    'db_hostname': 'localhost',
    'db_port': 5432
}
connection = Connection(**db_config)
