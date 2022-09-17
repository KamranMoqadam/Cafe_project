from peewee import *
import back_end.core.db_connection as database_connection
import utils as val

db = PostgresqlDatabase('postgres', host='gina.iran.liara.ir', port=33704, user='root',
                        password='nhmlvrFkHKBA5jxjb9rycf1w')


class Category(Model):
    category_id = AutoField()
    category_name = CharField(max_length=255, unique=True)
    meal = CharField(max_length=255, unique=True)

    class Meta:
        database = database_connection.db_conn.db
        db_table = 'Category_model'

    def save_category(self):
        with database_connection.db_conn.db:
            print(self)
            if not self.table_exists():
                database_connection.db_conn.db.create_tables([self])

            val.Validator.valid_category = self
            val.Validator.validate()
            self.save()
            return 'ok'


if __name__ == '__main__':
    db.connect()
    db.create_tables([Category], safe=True)
