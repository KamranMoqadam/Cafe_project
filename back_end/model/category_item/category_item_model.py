import datetime
from peewee import *
import back_end.core.db_connection as database_connection
from back_end.model.category.category_model import Category
from back_end.model.item.item_model import Menu_Item


class Category_item(Model):
    category_id = ForeignKeyField(Category, on_delete='CASCADE', on_update='CASCADE', backref='categorys')
    menu_item_id = ForeignKeyField(Menu_Item, on_delete='CASCADE', on_update='CASCADE', backref='menuitems')

    class Meta:
        database = database_connection.db_conn.db
        db_table = 'category_item'

    def save_category_item(self):
        with database_connection.db_conn.db:
            if not self.table_exists():
                database_connection.db_conn.db.create_tables([self])

            # val.Validator.valid_order = self
            # val.Validator.validate()
            self.save()
            return 'ok'

cat = Category_item(category_id=Category.get(Category.category_id==1),menu_item_id=Menu_Item.get(Menu_Item.menu_id==1))
cat.save_category_item()
