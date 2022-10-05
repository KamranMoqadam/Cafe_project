import datetime
from peewee import *
import back_end.core.db_connection as database_connection
from back_end.model.users.users_model import Users
from back_end.model.item.item_model import Menu_Item
import back_end.model.comment.utiles as val


class Comment(Model):
    comment_id = AutoField()
    user_id = ForeignKeyField(Users, on_delete='CASCADE', on_update='CASCADE', backref='orders')
    menu_id = ForeignKeyField(Menu_Item, on_delete='CASCADE', on_update='CASCADE', backref='tables')
    comment_text = CharField()
    rate = IntegerField()
    comment_date = TimestampField(default=datetime.datetime.now())

    class Meta:
        database = database_connection.db_conn.db
        db_table = 'comment'

    def save_comment(self):
        with database_connection.db_conn.db:
            if not self.table_exists():
                database_connection.db_conn.db.create_tables([self])
            val.Validator.valid_comment = self
            val.Validator.validate()
            self.save()
            return 'ok'

