from back_end.model.tables import table_model
from table_model import tables
from ..log import cafe_log

class Validator:
    valid_table: table_model.tables

    @classmethod
    def validate(cls):
        if isinstance(cls.valid_table.table_number, int):
            cafe_log.error("invalid take table number")
            raise ValueError("invalid table number")
        if isinstance(cls.valid_table.capacity, int):
            cafe_log.error("invalid take capcity")
            raise ValueError("invalid capacity")
        if isinstance(cls.valid_table.booking, bool):
            cafe_log.error("invalid take booking")
            raise ValueError("invalid booking")
        
