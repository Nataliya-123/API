import os.path
import pytest
import requests
from api import Pets

pt = Pets()


def test_get_registered():
    status = pt.get_registered()[0]
    detail = pt.get_registered()[1]
    assert status == 400
    assert detail =='Username is taken or pass issue'

'''Проверка ответа при регистрации зарегистрированнного пользователя'''


def test_get_token():
    status = pt.get_token()[3]
    token = pt.get_token()[0]
    assert token
    assert status == 200


def test_list_users():
    status = pt.get_list_users()[0]
    my_id = pt.get_list_users()[1]
    assert status == 200
    assert my_id


def test_save_pet():
    status = pt.get_save_pet()[0]
    pet_id = pt.get_save_pet()[1]
    assert status == 200
    assert pet_id


@pytest.mark.xfail
def test_pet_id():
    status = pt.get_pet_id()[0]
    id_pet = pt.get_pet_id()[1]
    name_pet = pt.get_pet_id()[2]
    gender = pt.get_pet_id()[3]
    owner_id = pt.get_pet_id()[4]
    assert status == 200
    assert id_pet == pt.get_save_pet()[1]
    assert name_pet
    assert gender == 'Male'
    assert owner_id == pt.get_token()[1]
'''При отправке запроса кроме того, что возвращаются данные по id питомца, так и создаётся новый питомец. Из за этого падает assert id_pet'''


def test_get_pet_by_usr_id():
    status = pt.get_pet_by_usr_id()[0]
    list1 = pt.get_pet_by_usr_id()[1]
    assert status == 200
    assert list1

@pytest.mark.xfail
def test_add_like():
    status = pt.add_like()
    assert status == 200
'''Для питомца, у которого проставлен лайк юзером можно поставить второй этим же юзером без возвращения ошибки'''

def test_add_comment():
    status = pt.add_comment()[0]
    id_comment = pt.add_comment()[1]
    assert status == 200
    assert id_comment


def test_pet_delete():
    status = pt.pet_delete()
    assert status == 200
