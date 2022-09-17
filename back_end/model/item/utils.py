import item_model
from back_end.log.log import cafe_log


class Validator:
    valid_item: item_model.Item

    @staticmethod
    def validate(cls):
        if isinstance(cls.valid_item.item_name, str):
            cafe_log.error("invalid item name")
            raise ValueError("invalid item name")
        if isinstance(cls.valid_item.price, str):
            cafe_log.error("invalid price")
            raise ValueError("invalid price")
        if isinstance(cls.valid_item.category, str):
            cafe_log.error("invalid category")
            raise ValueError("invalid category")
        if isinstance(cls.valid_item.menu_id, item_model.Item):
            cafe_log.error("invalid menu id")
            raise ValueError("invalid menu id")
