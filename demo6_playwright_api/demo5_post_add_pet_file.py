from playwright.sync_api import sync_playwright
import json
# test_add_valid_pet()
# test_add_invalid_pet() 

with open("test_data/pet.json","r") as file:
    payload=json.load(file)

print(payload["addPet"])

with sync_playwright() as p:
    api_context = p.request.new_context(base_url="https://petstore.swagger.io/v2/")

    response = api_context.post("pet",data=payload["addPet"],headers={"Content-Type":"application/json","api_key":"special-key"})

    print(response.status)
    print(response.json())

    assert response.json()["id"]==855
    assert response.status==200
    # assert response.ok

