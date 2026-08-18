from playwright.sync_api import sync_playwright
import json


with open("test_data/new_pet.json","r") as file:
    payload=json.load(file)

# print(payload)
# print(payload["id"])

with sync_playwright() as p:
    api_context = p.request.new_context(base_url="https://petstore.swagger.io/v2/")

    response = api_context.post("pet",data=payload,headers={"Content-Type":"application/json","api_key":"special-key"})

    print(response.status)
    print(response.json())

    assert response.json()["id"]==855
    assert response.status==200
    # assert response.ok

