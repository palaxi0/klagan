
import requests

base_url = 'https://petstore.swagger.io/v2'
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}
payload = {
    "id": 1010,
    "username": "Pipepal_S",
    "firstName": "Palacio",
    "lastName": "Palacio",
    "email": "palaxis08@gmail.com",
    "password": "Nodalaclave1",
    "phone": "3166225559",
    "userStatus": 0
  }

def test_create_new_user():
    response = requests.post(
        f"{base_url}/user",
        headers=headers,
        json=payload
    )
    assert response.status_code == 200

def test_get_username():
    response = requests.get(
        f"{base_url}/user/Pipepal_S",
        headers=headers,
        json=payload
    )
    assert response.status_code == 200


def test_get_sold_pets():
    response = requests.get(f'{base_url}/pet/findByStatus?status=sold')
    if response.status_code == 200:
        data = response.json()
        sold_pets = [(pet["id"], pet["name"]) for pet in data]
        pet_counter = CounterPetNames(sold_pets)
        print(pet_counter.count_names())


class CounterPetNames:

    def __init__(self, sold_pets):
        self.sold_pets = sold_pets

    def count_names(self):
        dict_counter = {}
        for data in self.sold_pets:
            name = data[1]
            if name not in dict_counter:
                dict_counter[name] = 1
            else:
                dict_counter[name] += 1

        return dict_counter






