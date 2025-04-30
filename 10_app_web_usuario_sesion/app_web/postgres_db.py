

from psycopg2.pool import ThreadedConnectionPool
from contextlib import contextmanager

db_config = { "host" : "localhost",
                "database" : "sistema_abc",
                "user" : "uacm",
                "password" : "uacm1"}


_tabla_productos = "CREATE TABLE Productos (" \
                "id SERIAL PRIMARY KEY,"  \
                "descripcion TEXT,"   \
                "precio NUMERIC(10, 2)" \
                ");"


class PostgresDB:
    def __init__(self):
        self.app = None
        self.pool = None

    def init_app(self, app):
        self.app = app
        self.connect()

    def connect(self):
        self.pool = ThreadedConnectionPool(minconn=1, maxconn=30, **db_config)

    def create_all_tables(self):
        drop_productos ="DROP TABLE IF EXISTS Productos;"
        with self.get_cursor() as cur: 
            cur.execute(drop_productos)
            cur.execute(_tabla_productos)

    @contextmanager
    def get_cursor(self):
        if self.pool is None:
            self.connect()
        con = self.pool.getconn()
        try:
            yield con.cursor()
            con.commit()
        finally:
            self.pool.putconn(con)