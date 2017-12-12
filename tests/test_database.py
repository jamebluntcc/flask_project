import pytest
from app.db import DB

@pytest.fixture
def setup():
    cmd = 'delete from haha'
    db = DB()
    db.execute(cmd)
    db.insert_all('haha', [{'NAME': 'chencheng'},
                           {'NAME': 'lxgui'},
                           {'NAME': 'liuhao'}])


def test_update():
    setup()
    db = DB()
    result = db.update('haha', {'NAME': 'cc'}, {'NAME': 'chencheng'})
    assert result is None




