import datetime
from peewee import *
import back_end.core.db_connection as database_connection
# from ..users.users_model import users_model
from back_end.model.order.utils import Validator
from back_end.model.tables.table_model import tables
from back_end.model.users.users_model import Users
from back_end.model.item.item_model import Menu_Item


class orders(Model):
    order_id = AutoField()
    user_id = ForeignKeyField(Users, on_delete='CASCADE', on_update='CASCADE', backref='orders')
    table_id = ForeignKeyField(tables, on_delete='CASCADE', on_update='CASCADE', backref='tables', null=True)
    item_id = ForeignKeyField(Menu_Item, on_delete='CASCADE', on_update='CASCADE', backref='items')
    number = CharField()
    count = IntegerField()
    status = CharField()
    takeaway = BooleanField()
    ready_time = TimestampField()
    order_date = TimestampField(default=datetime.datetime.now())

    class Meta:
        database = database_connection.db_conn.db
        db_table = 'orders'

    @staticmethod
    def save_orders(data):
        with database_connection.db_conn.db:
            if not orders.table_exists():
                database_connection.db_conn.db.create_tables([orders])

            # Validator.valid_order = orders
            # Validator.validate()

            orders.insert_many(data).execute()
            return 'ok'
