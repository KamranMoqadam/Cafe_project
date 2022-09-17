import datetime
from peewee import *
import back_end.core.db_connection as database_connection
# from ..users.users_model import users_model
# from ..item.item_model import item_model
import back_end.model.comment.utiles as val

db = PostgresqlDatabase('postgres', host='gina.iran.liara.ir', port=33704, user='root',
                        password='nhmlvrFkHKBA5jxjb9rycf1w')


class users(Model):
    id: int


class item(Model):
    id: int



class comment(Model):
    comment_id = AutoField()
    user_id = ForeignKeyField(users, on_delete='CASCADE', on_update='CASCADE', backref='orders')
    menu_id = ForeignKeyField(item, on_delete='CASCADE', on_update='CASCADE', backref='tables')
    comment_text = CharField()
    rate = IntegerField()
    comment_date = TimestampField(default=datetime.datetime.now())

    class Meta:
        database = database_connection.db_conn.db
        db_table = 'comment'

    def save_orders(self):
        with database_connection.db_conn.db:
            print(self)
            if not self.table_exists():
                database_connection.db_conn.db.create_tables([self])

            val.Validator.valid_comment = self
            val.Validator.validate()
            self.save()
            return 'ok'



