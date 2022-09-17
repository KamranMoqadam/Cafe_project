from back_end.model.users.users_model import Users
from back_end.model.item.item_model import Menu_Item
from back_end.model.tables.table_model import tables
from back_end.model.log import cafe_log


class Validator:
    valid_order: any

    @classmethod
    def validate(cls):
        if not isinstance(cls.valid_order.takeaway, bool):
            cafe_log.error("invalid take away")
            raise ValueError("invalid take away")
        if not isinstance(cls.valid_order.number, int):
            cafe_log.error("invalid take number")
            raise ValueError("invalid number")
        if not isinstance(cls.valid_order.status, str):
            cafe_log.error("invalid take status")
            raise ValueError("invalid status")
        if not isinstance(cls.valid_order.user_id, Users):
            cafe_log.error("invalid take user id")
            raise ValueError("invalid user id")
        if not isinstance(cls.valid_order.item_id, Menu_Item):
            cafe_log.error("invalid take item id")
            raise ValueError("invalid take item id")
        if not isinstance(cls.valid_order.table_id, tables):
            cafe_log.error("invalid take table id")
            raise ValueError("invalid table id")
