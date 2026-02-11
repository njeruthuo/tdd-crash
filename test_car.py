import pytest

from car import Car, UserManager, Database

# ---------- TEST CAR LOGIC -------------


@pytest.fixture
def car() -> Car:
    return Car()


def test_car_start_speed(car):
    assert car.speed == 0


def test_change_default_speed(car):
    car.speed = 20
    assert car.speed == 20


def test_cannot_accept_negative_values(car):
    with pytest.raises(ValueError, match="Speed cannot be less than zero!"):
        car.speed = -10


def test_speed_limit(car):
    car.speed = 65
    assert car.speed_limit == "Safe Speed"

    car.speed = 100
    assert car.speed_limit == "Recommended speed"

    car.speed = 165
    assert car.speed_limit == "Over speeding"


# ------------TEST USERMANAGER LOGIC ------------
@pytest.fixture
def user_manager() -> UserManager:
    return UserManager()


def test_can_add_user(user_manager):
    assert user_manager.add_user("Julius", "juliusn411@gmail.com") == True
    assert user_manager.get_user("Julius") == "juliusn411@gmail.com"


def test_cannot_duplicate_username(user_manager):
    user_manager.add_user("Julius", "juliusn411@gmail.com")
    with pytest.raises(ValueError, match="User already exists"):
        user_manager.add_user("Julius", "njeruthelearner@gmail.com")


def test_getting_nonexistent_user(user_manager):
    assert user_manager.get_user(
        "Julius") == None, "A nonexistent user return `None`"


# ------------- TEST DATABASE LOGIC ----------------

@pytest.fixture
def db():
    """Provides a clean instance of the database and cleans up after the test"""
    database = Database()
    yield database
    database.data.clear()


def test_can_add_database_user(db):
    db.add_user(1, "Alice")
    assert db.get_user(1) == "Alice"


def test_can_add_duplicate_database_user(db):
    db.add_user(1, "Alice")
    with pytest.raises(ValueError, match="User already exists"):
        db.add_user(1, "Violet")


def test_delete_database_user(db):
    db.add_user(5, "Bob Marley")
    db.delete_user(5)
    assert db.get_user(5) is None
