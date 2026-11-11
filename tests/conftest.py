import hashlib
import sqlite3
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import database  # noqa: E402
from app import app as flask_app  # noqa: E402

USERS = {"ADMIN": "admin", "TEST": "123456", "ALICE": "alice"}


def _create_dbs(db_dir):
    users = sqlite3.connect(db_dir / "users.db")
    users.execute("CREATE TABLE users (id text primary key, pw text)")
    users.executemany(
        "INSERT INTO users VALUES (?, ?)",
        [(uid, hashlib.sha256(pw.encode()).hexdigest()) for uid, pw in USERS.items()],
    )
    users.commit()
    users.close()

    notes = sqlite3.connect(db_dir / "notes.db")
    notes.execute("CREATE TABLE notes (user text, timestamp text, note text, note_id text)")
    notes.commit()
    notes.close()

    images = sqlite3.connect(db_dir / "images.db")
    images.execute("CREATE TABLE images (uid text unique, owner text, name text, timestamp text)")
    images.commit()
    images.close()


@pytest.fixture
def client(tmp_path, monkeypatch):
    # Isolated databases and upload folder so tests never touch the real data
    db_dir = tmp_path / "db"
    db_dir.mkdir()
    _create_dbs(db_dir)
    upload_dir = tmp_path / "images"
    upload_dir.mkdir()

    monkeypatch.setattr(database, "user_db_file_location", str(db_dir / "users.db"))
    monkeypatch.setattr(database, "note_db_file_location", str(db_dir / "notes.db"))
    monkeypatch.setattr(database, "image_db_file_location", str(db_dir / "images.db"))
    flask_app.config.update(TESTING=True, UPLOAD_FOLDER=str(upload_dir))

    with flask_app.test_client() as c:
        yield c


@pytest.fixture
def login(client):
    def _login(user_id, password=None):
        password = password if password is not None else USERS[user_id.upper()]
        return client.post("/login", data={"id": user_id, "pw": password})

    return _login
