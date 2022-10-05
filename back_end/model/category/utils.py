import category_model
from back_end.models import cafe_log


class Validator:
    valid_category: category_model.Category

    @staticmethod
    def validate(cls):
        if isinstance(cls.valid_category.category_name, str):
            cafe_log.error("invalid category name")
            raise ValueError("invalid category name")
        if isinstance(cls.valid_category.meal, str):
            cafe_log.error("invalid meal")
            raise ValueError("invalid meal")
        if isinstance(cls.valid_category.category_id, category_model.Category):
            cafe_log.error("invalid category id")
            raise ValueError("invalid category id")
