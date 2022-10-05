
from back_end.model.users.users_model import Users
from back_end.model.item.item_model import Menu_Item
from back_end.model.log import cafe_log
import re


class Validator:
    valid_comment: any
    comment_text_regex = re.compile(r"\.{1,}")

    @classmethod
    def validate(cls):
        if not Validator.validate_userid(cls.valid_comment.user_id):
            cafe_log.error("invalid user id")
            raise ValueError("invalid user id")
        if not Validator.validate_menu_id(cls.valid_comment.menu_id):
            cafe_log.error("invalid menu id")
            raise ValueError("invalid menu id")
        if not Validator.validate_comment_text(cls.valid_comment.comment_text):
            cafe_log.error("invalid comment text")
            raise ValueError("invalid comment text")
        if not Validator.validate_comment_rate(cls.valid_comment.rate):
            cafe_log.error("invalid comment rate")
            raise ValueError("invalid comment rate")

    @staticmethod
    def validate_userid(user_id):
        if isinstance(user_id, Users):
            return True
        else:
            return False

    @staticmethod
    def validate_menu_id(menu_id):
        if isinstance(menu_id, Menu_Item):
            return True
        else:
            return False

    @staticmethod
    def validate_comment_text(comment_text):

        if len(comment_text)>0:
            return True
        else:
            return False

    @staticmethod
    def validate_comment_rate(comment_rate):
        if isinstance(comment_rate, int):
            if 0 <= comment_rate <= 10:
                return True
            else:
                return False
        else:
            return False
