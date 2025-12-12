from http import HTTPStatus


def test_root_should_return_ok_and_hello_world(client):
    response = client.get("/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "Hello World!"}


def test_should_create_an_new_user(client):
    response = client.post(
        "/users/",
        json={
            "username": "test",
            "email": "test@test.com",
            "password": "test",
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        "id": 1,
        "username": "test",
        "email": "test@test.com",
    }


def test_should_return_user_by_id(client):
    response = client.get("/users/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "id": 1,
        "username": "test",
        "email": "test@test.com",
    }


def test_should_return_not_found_in_user_by_id(client):
    response = client.get("/users/4")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_should_return_a_user_list(client):
    response = client.get("/users/")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "users": [{"username": "test", "email": "test@test.com", "id": 1}]
    }


def test_update_user(client):
    response = client.put(
        "/users/1",
        json={
            "username": "Test",
            "email": "test@example.com",
            "password": "mynewpassword",
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        "username": "Test",
        "email": "test@example.com",
        "id": 1,
    }


def test_update_user_should_return_not_found(client):
    response = client.put(
        "/users/5",
        json={
            "username": "Test",
            "email": "test@example.com",
            "password": "mynewpassword",
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}


def test_delete_user(client):
    response = client.delete("/users/1")
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {"message": "User deleted"}


def test_delete_user_should_return_not_found(client):
    response = client.delete("/users/4")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {"detail": "User not found"}
