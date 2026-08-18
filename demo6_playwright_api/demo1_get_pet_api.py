from playwright.sync_api import sync_playwright

# test_search_valid_pet_id
# test_search_invalid_pet_id


with sync_playwright() as p:
    api_context = p.request.new_context(
        base_url="https://petstore.swagger.io/v2/")

    response = api_context.get("pet/999")

    print(response.status)
    print(response.status_text)
    print(response.json())
    print(response.text())
    print(response.headers)

    print(response.headers)
    print(response.headers["date"])

    # kind of dic right now
    response_body = response.json()

    print(response_body["id"])
    print(response_body["name"])
    print(response_body["status"])
    print(response_body["category"])
    print(response_body["category"]["id"])
    print(response_body["category"]["name"])

    # print id and name from tags
    print(response_body["tags"])
    print(response_body["tags"][0])
    print(response_body["tags"][0]['id'])
    print(response_body["tags"][0]['name'])
