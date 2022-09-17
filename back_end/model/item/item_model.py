import datetime
from peewee import *
import back_end.core.db_connection as database_connection


class Menu_Item(Model):
    menu_id = AutoField()
    item_name = CharField(max_length=255, unique=True)
    price = CharField()
    discount = CharField(default=0)
    serving_time = TimestampField(default=datetime.datetime.now())
    cooking_time = TimestampField(default=datetime.datetime.now())

    class Meta:
        database = database_connection.db_conn.db
        db_table = 'menu_item'

    def save_Item(self):
        with database_connection.db_conn.db:
            print(self)
            if not self.table_exists():
                database_connection.db_conn.db.create_tables([self])

            # val.Validator.valid_item = self
            # val.Validator.validate()
            self.save()
            return 'ok'


