from back_end.model.comment import comment_model
from ..users.users_model import users
from ..item.item_model import item
from ..log import cafe_log
import re


class Validator:
    valid_comment: comment_model.comment
    comment_text_regex = re.compile(r"\.{1,}")
    @classmethod
    def validate(cls):
        if Validator.validate_userid(cls.valid_comment.user_id) != True:
            cafe_log.error("invalid user id")
            raise ValueError("invalid user id")
        if Validator.validate_menu_id(cls.valid_comment.menu_id) != True:
            cafe_log.error("invalid menu id")
            raise ValueError("invalid menu id")
        if Validator.validate_comment_text(cls.valid_comment.comment_text) != True:
            cafe_log.error("invalid comment text")
            raise ValueError("invalid comment text")
        if Validator.validate_comment_rate(cls.valid_comment.rate) != True:
            cafe_log.error("invalid comment rate")
            raise ValueError("invalid comment rate")

    @staticmethod
    def validate_userid(user_id):
        if isinstance(user_id, users):
            return True
        else:
            return False

    @staticmethod
    def validate_menu_id(menu_id):
        if isinstance(menu_id, item):
            return True
        else:
            return False

    @staticmethod
    def validate_comment_text(comment_text):
        if Validator.comment_text_regex.match(comment_text):
            return True
        else:
            return False

    @staticmethod
    def validate_comment_rate(comment_rate):
        if isinstance(comment_rate,int):
            if 0<=comment_rate<=10:
                return True
            else:
                return False
        else:
            return False
