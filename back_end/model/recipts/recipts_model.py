from email.policy import default
from peewee import *
import back_end.core.db_connection as database_connection
import back_end.model.recipts.utils as val
from ..order.oredr_model import orders
import datetime

class users(Model):
    id: int
    
    
class receipts(Model):
    receipts_id = AutoField()
    order_id = ForeignKeyField(orders, on_delete='CASCADE', on_update='CASCADE', backref='orders')
    user_id = ForeignKeyField(users, on_delete='CASCADE', on_update='CASCADE', backref='orders')
    total_price = CharField()
    final_price = CharField(default=total_price)
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
