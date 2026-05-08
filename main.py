import requests
from handlers import error_handler

BASE_URL = 'https://dummyjson.com/products'

@error_handler
def get_all_products():
    response = requests.get(f"{BASE_URL}", timeout=5)
    return response

@error_handler
def get_single_product(prod_id: int):
    response = requests.get(f"{BASE_URL}/{prod_id}", timeout=5)
    return response

@error_handler
def get_product_category(prod_category: str):
    response = requests.get(f"{BASE_URL}/category/{prod_category}")
    return response

@error_handler
def search_product(some_param: str):
    params = {
        'q': some_param
    }
    response = requests.get(f"{BASE_URL}/search", params=params)
    return response

@error_handler
def sort_product(some_param: str, asc_desc='asc'):
    params = {
        'sortBy': some_param,
        'order': asc_desc
    }
    response = requests.get(f'{BASE_URL}', params=params)
    return response

@error_handler
def add_product(title: str, descript: str):
    response = requests.post(
        f'{BASE_URL}/add',
        headers={'Content-Type': 'application/json'},
        json={'title': title, 'description': descript}
    )
    return response

@error_handler
def delete_product(prod_id: int):
    response = requests.delete(f'{BASE_URL}/{prod_id}')
    return response

print(get_all_products().json())
print(search_product('product').json())
print(add_product('Some product', 'Some description').text)
