from back_end.model.recipts import recipts_model
from ..log import cafe_log

class Validator:
    valid_receipt: recipts_model.receipts

    @classmethod
    def validate(cls):
        if isinstance(cls.valid_receipt.order_id, int):
            cafe_log.error("invalid take order id")
            raise ValueError("invalid order id")
        if isinstance(cls.valid_receipt.user_id, int):
            cafe_log.error("invalid take user id")
            raise ValueError("invalid user id")
        if isinstance(cls.valid_receipt.total_price, str):
            cafe_log.error("invalid take total price")
            raise ValueError("invalid total price")
        if isinstance(cls.valid_receipt.final_price, str):
            cafe_log.error("invalid take final_price")
            raise ValueError("invalid final_price")
    
        