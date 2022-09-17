import datetime
from peewee import *
import back_end.core.db_connection as database_connection
# from ..users.users_model import users_model
import back_end.model.order.utils as val

db = PostgresqlDatabase('postgres', host='gina.iran.liara.ir', port=33704, user='root',
                        password='nhmlvrFkHKBA5jxjb9rycf1w')


class users(Model):
    id: int


class tables(Model):
    id: int


class item(Model):
    id: int


class orders(Model):
    order_id = AutoField()
    user_id = ForeignKeyField(users, on_delete='CASCADE', on_update='CASCADE', backref='orders')
    table_id = ForeignKeyField(tables, on_delete='CASCADE', on_update='CASCADE', backref='tables')
    item_id = ForeignKeyField(item, on_delete='CASCADE', on_update='CASCADE', backref='items')
    number = IntegerField()
    status = CharField()
    takeaway = BooleanField()
    order_date = TimestampField(default=datetime.datetime.now())

    class Meta:
        database = database_connection.db_conn.db
        db_table = 'orders'

    def save_orders(self):
        with database_connection.db_conn.db:
            print(self)
            if not self.table_exists():
                database_connection.db_conn.db.create_tables([self])

            val.Validator.valid_order = self
            val.Validator.validate()
            self.save()
            return 'ok'



