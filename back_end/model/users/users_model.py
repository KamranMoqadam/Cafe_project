from back_end.core.db_connection import db_conn
from peewee import *


class Users(Model):
    user_id = AutoField()
    first_name = CharField()
    last_name = CharField()
    phone = CharField(unique=True)
    email = CharField()
    address = CharField()
    password = CharField()
    type = CharField()

    class Meta:
        database = db_conn.db
        db_table = 'users'

    def save_users(self):
        with db_conn.db:
            if not self.table_exists():
                db_conn.db.create_tables([self])

            # val.Validator.valid_users = self
            # val.Validator.validate()
            self.save()
            return 'user created!'



