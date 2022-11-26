import requests
import json
from local_settings import VALID_EMAIL
from local_settings import VALID_PASSWORD


class Pets:
    def __init__(self):
        self.base_url = 'http://34.141.58.52:8000/'

    def get_registered(self) -> json:
        '''Регистрация пользователя'''
        data = {"email": '8646477@mall661.ru',
                "password": '1234', "confirm_password": '1234'}
        res = requests.post(self.base_url + 'register', data=json.dumps(data))
        Jsondata = res.json()
        #reg_id1 = Jsondata.get('id')
        status = res.status_code
        #token_reg1 = Jsondata.get('token')
        detail = res.json()['detail']


        return status, detail



    # def delete_user(self) -> json:
    #     token = Pets().get_registered()[2]
    #     reg = Pets().get_registered()[1]
    #     headers = {'Authorization': f'Bearer {token}'}
    #     res = requests.delete(self.base_url + f'users/{reg}', headers=headers)
    #     status = res.status_code
    #     print(status)
    #     return status

    def get_token(self) -> json:
        '''Запрос на получение авторизацию'''
        data = {
            "password": VALID_PASSWORD,
            "email": VALID_EMAIL
        }
        res = requests.post(self.base_url + 'login', data=json.dumps(data))
        my_token = res.json()['token']
        my_id = res.json()['id']
        my_email = res.json()['email']
        status = res.status_code

        return my_token, my_id, my_email, status

    def get_list_users(self) -> json:
        '''Запрос для получения списка юзеров, но по факту для получения нашего id'''
        my_token = Pets().get_token()[0]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + 'users', headers=headers)
        status = res.status_code
        my_id = res.json
        return status, my_id




    def get_save_pet(self) -> json:
        '''Запрос на добавление питомца'''
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {
            "name": "Nelsonbbbbbb",
            "type": "dog",
            "age": 2,
            "gender": "Male",
            "owner_id": my_id,
            "likes_count": None,
            "liked_by_user": False
        }
        res = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        pet_id = res.json()['id']
        status = res.status_code
        return status, pet_id

    def get_pet_id(self) -> json:
        '''Запрос на получение информации по питомцу по его id'''
        my_token = Pets().get_token()[0]
        pet_id = Pets().get_save_pet()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        status = res.status_code
        id_pet = res.json()['pet']['id']
        name_pet = res.json()['pet']['name']
        gender = res.json()['pet']['gender']
        owner_id = res.json()['pet']['owner_id']
        type = res.json()['pet']['type']
        return status, id_pet, name_pet, gender, owner_id, type

    def get_pet_by_usr_id(self) -> json:
        '''Запрос на получение  всех питомцев юзера'''
        my_token = Pets().get_token()[0]
        my_id = Pets().get_token()[1]
        pet_id = Pets().get_save_pet()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {
            "skip": 0,
            "num": 10,
            "type": "dog",
            "petName": None,
            "user_id": my_id
        }
        res = requests.post(self.base_url + 'pets', data=json.dumps(data), headers=headers)
        status = res.status_code
        list = res.json()
        return status, list

    def add_like(self) -> json:
        '''Запрос на добавление лайка последнему созданному питомцу'''
        my_token = Pets().get_token()[0]
        pet_id = Pets().get_save_pet()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {"id": Pets().get_save_pet()[1]}
        res = requests.put(self.base_url + f'pet/{pet_id}/like', data=json.dumps(data), headers=headers)
        status = res.status_code
        return status

    def add_comment(self) -> json:
        '''Запрос на добавление комментария последнему созданному питомцу  возвращения ай ди комментария'''
        my_token = Pets().get_token()[0]
        pet_id = Pets().get_save_pet()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        data = {
            "message": "это комментрий",
            "pet_id": pet_id,
            "date": "1946-10-27T04:05:22.571Z",
            "user_id": 218,
            "user_name": "chelyadinskaya1@mail.ru"
        }
        res = requests.put(self.base_url + f'pet/{pet_id}/comment', data=json.dumps(data), headers=headers)
        status = res.status_code
        id_comment = res.json()['id']
        return status, id_comment


    def pet_delete(self)-> json:
        '''Запрос на удаления питомца, созданного в апи get_save_pet '''
        my_token = Pets().get_token()[0]
        pet_id = Pets().get_save_pet()[1]
        headers = {'Authorization': f'Bearer {my_token}'}
        res = requests.delete(self.base_url + f'pet/{pet_id}', headers=headers)
        status=res.status_code
        return status


Pets().get_token()
Pets().get_list_users()
Pets().get_save_pet()
Pets().get_pet_id()
Pets().get_pet_by_usr_id()
Pets().add_like()
Pets().add_comment()
Pets().pet_delete()
Pets().get_registered()
# Pets().delete_user()

