from dataclasses import asdict
from fast_zero.models import User
from sqlalchemy import select


def test_create_user(session, mock_db_time):
    with mock_db_time(model=User) as time:
        new_user = User(
            username="testex", email="testex@testex.com", password="testex"
        )
        session.add(new_user)
        session.commit()

    user = session.scalar(select(User).where(User.username == "testex"))

    assert asdict(user) == {
        "id": 1,
        "username": "testex",
        "email": "testex@testex.com",
        "password": "testex",
        "created_at": time,
        "updated_at": time,
    }
