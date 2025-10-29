# Task_1
"""Створіть метод класу з назвою `validate`, який має викликатися з методу `__init__` для перевірки параметра email, 
переданого конструктору. Логіка всередині методу `validate` може полягати в перевірці, чи є переданий параметр email 
коректним рядком електронної пошти"""

import re

class User:
    def __init__(self, email):              # метод класу validate перед збереженням email
        self.email = self.validate(email)

    @classmethod

    def validate(cls, email):
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'   # Чи є email коректним за форматом""
        if not re.match(pattern, email):
            raise ValueError(f"Невірна адреса електронної пошти: {email}")
        return email

user1 = User("olenkabeka@egmail.com")
print(user1.email)  

try:
    user2 = User("wrong-email")
    print(user2.email)
except ValueError as e:
    print(e)  
