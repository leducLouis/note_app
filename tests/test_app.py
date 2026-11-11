def test_home_page(client):
    assert client.get("/").status_code == 200


def test_private_requires_login(client):
    assert client.get("/private/").status_code == 401


def test_login_success(client, login):
    login("test")
    with client.session_transaction() as sess:
        assert sess["current_user"] == "TEST"


def test_login_wrong_password(client, login):
    login("test", "wrong")
    with client.session_transaction() as sess:
        assert "current_user" not in sess


def test_login_unknown_user(client, login):
    login("nobody", "whatever")
    with client.session_transaction() as sess:
        assert "current_user" not in sess


def test_logout(client, login):
    login("test")
    client.get("/logout/")
    with client.session_transaction() as sess:
        assert "current_user" not in sess


def test_write_note_shows_on_private_page(client, login):
    login("test")
    client.post("/write_note", data={"text_note_to_take": "Acheter du pain"})
    page = client.get("/private/")
    assert page.status_code == 200
    assert "Acheter du pain" in page.get_data(as_text=True)


def test_notes_are_isolated_between_users(client, login):
    login("test")
    client.post("/write_note", data={"text_note_to_take": "Note privee de TEST"})
    client.get("/logout/")

    login("alice")
    page = client.get("/private/").get_data(as_text=True)
    assert "Note privee de TEST" not in page


def test_admin_page_forbidden_for_regular_user(client, login):
    login("test")
    assert client.get("/admin/").status_code == 401


def test_admin_page_lists_users(client, login):
    login("admin")
    page = client.get("/admin/").get_data(as_text=True)
    assert "TEST" in page and "ALICE" in page


def test_admin_can_add_user(client, login):
    login("admin")
    client.post("/add_user", data={"id": "bob", "pw": "bob"})
    page = client.get("/admin/").get_data(as_text=True)
    assert "BOB" in page
