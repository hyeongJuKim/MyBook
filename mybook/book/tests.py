import pytest
from .models import User, Book


# test sample
def test_hello_world():
    assert "hello_world" == "hello_world"

@pytest.mark.django_db
def test_user_count():
    assert User.objects.count() == 0

@pytest.mark.django_db
def test_user_create_without_email():
    with pytest.raises(ValueError):
        me = User.objects.create_user(name="강현구", email="")
        me.save()


@pytest.mark.django_db
def test_user_create():
    me = User.objects.create_user(email="rkdgusrnrlrl@gmail.com", name="강현구", nick_name="rkdgusrnrlrl")
    me.save()
    assert User.objects.count() == 1


def test_hello_hj():
    assert 'hello_hj' == 'hello_hj'


@pytest.mark.django_db
def test_create_book():
    test_user_create()

    me = User.objects.get(id=1)
    book = Book(title='처음산책', contents='작정하고 샀습니다', user=me)
    book.save()
    assert Book.objects.count() == 1


@pytest.mark.django_db
def test_get_book():
    test_create_book()

    book = Book.objects.get(id=1, title='처음산책')
    assert book.title == '처음산책'


@pytest.mark.django_db
def test_modify_book():
    test_create_book()

    book = Book.objects.get(id=1, title='처음산책')
    book.contents = '잘샀네'
    book.save()
    assert book.contents == '잘샀네'


@pytest.mark.django_db
def test_delete_book():
    test_create_book()

    book = Book.objects.get(id=1, title='처음산책')
    book.delete()
    book.save
    assert Book.objects.all().count() == 0

