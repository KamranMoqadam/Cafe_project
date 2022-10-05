from peewee import *


class db_conn():
    db = PostgresqlDatabase('postgres', host='gina.iran.liara.ir', port=33704, user='root',
                            password='nhmlvrFkHKBA5jxjb9rycf1w')
