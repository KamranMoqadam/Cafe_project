from back_end.core.db_connection import db_conn
import datetime

from peewee import *
# from ..users.users_model import users_model



class users(Model):
    id: int


class tables(Model):
    id: int


class item(Model):
    id: int


class Users(Model):
    user_id = AutoField()
    first_name = CharField()
    last_name = CharField()
    phone = CharField()
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

            # val.Validator.valid_order = self
            # val.Validator.validate()
            self.save()
            return 'user created!'


user_1 = Users(first_name="ADIB", last_name="Zandkarimi", phone="09123456789", email="adib@gmail.com", address="Sanandaj", password="876987", type="customer")


user_1.save_users()
