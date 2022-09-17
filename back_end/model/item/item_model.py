import utils as val
import datetime
from peewee import *
import back_end.core.db_connection as database_connection

db = PostgresqlDatabase('postgres', host='gina.iran.liara.ir', port=33704, user='root',
                        password='nhmlvrFkHKBA5jxjb9rycf1w')


class Item(Model):
    menu_id = AutoField()
    item_name = CharField(max_length=255, unique=True)
    price = CharField()
    category = CharField(max_length=255, unique=True)
    discount = CharField(default=0)
    serving_time = TimestampField(default=datetime.datetime.now())
    cooking_time = TimestampField(default=datetime.datetime.now())
    category_id = ForeignKeyField(category, on_delete='CASCADE', on_update='CASCADE', backref='category_id')

    class Meta:
        database = database_connection.db_conn.db
        db_table = 'item_model'

    def save_Item(self):
        with database_connection.db_conn.db:
            print(self)
            if not self.table_exists():
                database_connection.db_conn.db.create_tables([self])

            val.Validator.valid_item = self
            val.Validator.validate()
            self.save()
            return 'ok'


if __name__ == '__main__':
    db.connect()
    db.create_tables([Item], safe=True)
