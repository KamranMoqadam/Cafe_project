from back_end.model.order import oredr_model
from ..users.users_model import users
from ..item.item_model import item
from ..tables.table_model import tables
from ..log import cafe_log

class Validator:
    valid_order: oredr_model.orders

    @classmethod
    def validate(cls):
        if isinstance(cls.valid_order.takeaway, bool):
            cafe_log.error("invalid take away")
            raise ValueError("invalid take away")
        if isinstance(cls.valid_order.number, int):
            cafe_log.error("invalid take number")
            raise ValueError("invalid number")
        if isinstance(cls.valid_order.status, str):
            cafe_log.error("invalid take status")
            raise ValueError("invalid status")
        if isinstance(cls.valid_order.user_id, users):
            cafe_log.error("invalid take user id")
            raise ValueError("invalid user id")
        if isinstance(cls.valid_order.item_id, item):
            cafe_log.error("invalid take item id")
            raise ValueError("invalid take item id")
        if isinstance(cls.valid_order.table_id, tables):
            cafe_log.error("invalid take table id")
            raise ValueError("invalid table id")
