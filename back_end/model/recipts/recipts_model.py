from email.policy import default
from peewee import *
import back_end.core.db_connection as database_connection
import back_end.model.recipts.utils as val
from back_end.model.order.oredr_model import orders
from back_end.model.users.users_model import Users
import datetime


class receipts(Model):
    receipts_id = AutoField()
    order_id = ForeignKeyField(orders, on_delete='CASCADE', on_update='CASCADE', backref='orders')
    user_id = ForeignKeyField(Users, on_delete='CASCADE', on_update='CASCADE', backref='orders')
    total_price = CharField()
    final_price = CharField()
    receipts_date = TimestampField(default=datetime.datetime.now())

    class Meta:
        database = database_connection.db_conn.db
        db_table = 'receipts'

    def save_receipts(self):
        with database_connection.db_conn.db:
            print(self)
            if not self.table_exists():
                database_connection.db_conn.db.create_tables([self])

            val.Validator.valid_receipt = self
            val.Validator.validate()
            self.save()
            return 'ok'


c = receipts(order_id=orders.get(orders.order_id == 1), user_id=Users.get(Users.user_id == 1), total_price='200000',final_price='200000')
c.save_receipts()