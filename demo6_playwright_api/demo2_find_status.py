from playwright.sync_api import sync_playwright

# test_search_valid_status
# test_search_invalid_status


with sync_playwright() as p:
    api_context = p.request.new_context(
        base_url="https://petstore.swagger.io/v2/")

    response = api_context.get("pet/findByStatus?status=sold")

    print(response.status)
    print(response.json())

    response_body=response.json()
    print(response_body[0]['status'])
    print(len(response_body))

    # write for loop to print each status 
