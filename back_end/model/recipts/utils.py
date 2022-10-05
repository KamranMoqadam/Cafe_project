from back_end.model.log import cafe_log
from back_end.model.users.users_model import Users
from back_end.model.order.oredr_model import orders


class Validator:
    valid_receipt: any

    @classmethod
    def validate(cls):
        if not isinstance(cls.valid_receipt.order_id, orders):
            cafe_log.error("invalid take order id")
            raise ValueError("invalid order id")
        if not isinstance(cls.valid_receipt.user_id, Users):
            cafe_log.error("invalid take user id")
            raise ValueError("invalid user id")
        if not isinstance(cls.valid_receipt.total_price, str):
            cafe_log.error("invalid take total price")
            raise ValueError("invalid total price")
        if not isinstance(cls.valid_receipt.final_price, str):
            cafe_log.error("invalid take final_price")
            raise ValueError("invalid final_price")

