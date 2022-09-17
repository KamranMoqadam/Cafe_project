from peewee import *
import back_end.core.db_connection as database_connection
from back_end.model.tables.utils import Validator


class tables(Model):
    table_id = AutoField()
    table_number = IntegerField()
    capacity = IntegerField()
    booking = BooleanField()

    class Meta:
        database = database_connection.db_conn.db
        db_table = 'tables'

    def save_tables(self):
        with database_connection.db_conn.db:
            if not self.table_exists():
                database_connection.db_conn.db.create_tables([self])

            Validator.valid_table = self
            Validator.validate()
            self.save()
            return 'ok'


tab = tables(table_number=20, capacity=5, booking=False)
tab.save_tables()
