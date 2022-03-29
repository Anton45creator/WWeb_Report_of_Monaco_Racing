import pytest
from main.app import *


@pytest.fixture(scope="class")
def prepare_db():
    MODELS = [Racer]
    test_db = SqliteDatabase(":memory:")
    test_db.bind(MODELS)
    test_db.connect()
    test_db.create_tables(MODELS)
    yield
    test_db.drop_tables(MODELS)
    test_db.close()


client = app.test_client()