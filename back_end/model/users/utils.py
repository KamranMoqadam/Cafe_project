import re
from back_end.model.users.users_model import Users


class Validator:
    @staticmethod
    def valid_pass(value):
        pass_result = re.compile(r"\d{8}")
        if pass_result.match(str(value)):
            return value
        else:
            raise ValueError("Not accepted!")

    @staticmethod
    def valid_phone(num):
        accepted_phone = re.compile(r"^((\+98|0)9\d{9})$")
        print(num)
        print(accepted_phone.match(str(num)))
        if accepted_phone.match(str(num)):
            return num
        else:
            raise ValueError("Your phone number is not correct!")

    @staticmethod
    def valid_email(mail):
        accepted_email = re.compile(r"^[a-zA-Z0-9_]+@[a-z]+\.com$")
        if accepted_email.match(str(mail)):
            return mail
        else:
            raise ValueError("Your email address is not accepted!")


Validator.valid_phone(Users.phone)

