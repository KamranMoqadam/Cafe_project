
from back_end.model.log import cafe_log


class Validator:
    valid_table: any

    @classmethod
    def validate(cls):
        if not isinstance(cls.valid_table.table_number, int):
            cafe_log.error("invalid take table number")
            raise ValueError("invalid table number")
        if not isinstance(cls.valid_table.capacity, int):
            cafe_log.error("invalid take capcity")
            raise ValueError("invalid capacity")
        if not isinstance(cls.valid_table.booking, bool):
            cafe_log.error("invalid take booking")
            raise ValueError("invalid booking")
