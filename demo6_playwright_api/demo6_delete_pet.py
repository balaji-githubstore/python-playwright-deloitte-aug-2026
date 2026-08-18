from playwright.sync_api import sync_playwright

# test_search_valid_pet_id
# test_search_invalid_pet_id


with sync_playwright() as p:
    api_context = p.request.new_context(
        base_url="https://petstore.swagger.io/v2/")

    response = api_context.delete(
        "pet/999", headers={"api_key": "special-key"})

    print(response.status)
    # print(response.json())
