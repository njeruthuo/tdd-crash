from random import randint


class Car:
    def __init__(self):
        self._speed = 0

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value: int):
        if value < 0:
            raise ValueError("Speed cannot be less than zero!")
        self._speed = value

    @property
    def speed_limit(self):
        if self._speed > 80 and self._speed < 120:
            return "Recommended speed"
        elif self._speed < 80:
            return "Safe Speed"
        else:
            return "Over speeding"


class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, username, email):
        if username in self.users:
            raise ValueError("User already exists")
        self.users[username] = email
        return True

    def get_user(self, username):
        return self.users.get(username)


class Database:
    """Simulates a basic user database"""

    def __init__(self):
        self.data = {}  # simulate a real database in memory

    def add_user(self, user_id, name):
        if user_id in self.data:
            raise ValueError("User already exists")
        self.data[user_id] = name

    def get_user(self, user_id):
        return self.data.get(user_id)

    def delete_user(self, user_id):
        if user_id in self.data:
            del self.data[user_id]


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            print(
                f"{n} is {"not a " if n % i == 0 else "a "} prime because {n} % {i} == {n % i == 0}")
            return False
    return True
