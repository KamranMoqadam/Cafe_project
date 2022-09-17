from peewee import *
import back_end.core.db_connection as database_connection
import back_end.model.tables.utils as val


db = PostgresqlDatabase('postgres', host='gina.iran.liara.ir', port=33704, user='root',
                        password='nhmlvrFkHKBA5jxjb9rycf1w')

class tables(Model):
    table_id = AutoField()
    table_number = IntegerField()
    capacity = IntegerField()
    booking = BooleanField()
    
    class Meta:
        database = database_connection.db_conn.db
        db_table = 'tables'
        
    def save_orders(self):
        with database_connection.db_conn.db:
            print(self)
            if not self.table_exists():
                database_connection.db_conn.db.create_tables([self])

            val.Validator.valid_table = self
            val.Validator.validate()
            self.save()
            return 'ok'



