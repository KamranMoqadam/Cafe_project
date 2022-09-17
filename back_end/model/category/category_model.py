from peewee import *
import back_end.core.db_connection as database_connection


class Category(Model):
    category_id = AutoField()
    category_name = CharField(max_length=255, unique=True)
    meal = CharField(max_length=255, unique=True)

    class Meta:
        database = database_connection.db_conn.db
        db_table = 'category'

    def save_category(self):
        with database_connection.db_conn.db:
            if not self.table_exists():
                database_connection.db_conn.db.create_tables([self])
            #
            # val.Validator.valid_category = self
            # val.Validator.validate()
            self.save()
            return 'ok'


