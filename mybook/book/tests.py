import pytest
from .models import User

# test sample
def test_hello_world():
    assert "hello_world" == "hello_world"

@pytest.mark.django_db
def test_user_count():
    assert User.objects.count() == 0

@pytest.mark.django_db
def test_user_create():
    me = User(name="강현구", nick_name="rkdgusrnrlrl")
    me.save()
    assert User.objects.count() == 1
