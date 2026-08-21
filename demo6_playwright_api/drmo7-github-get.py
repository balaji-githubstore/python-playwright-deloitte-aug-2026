# List repositories for the authenticated user

from playwright.sync_api import sync_playwright
import json

with open("test_data/secret.json","r") as file:
    auth_token=json.load(file)

print(auth_token["token"])

with sync_playwright() as p:
    api_context = p.request.new_context(
        base_url="https://api.github.com/")

    response = api_context.get("user/repos",headers={"Authorization":f"Bearer {auth_token["token"]}",'Accept': 'application/vnd.github+json',})

    print(response.status)
    print(response.json())
    print(response.json()[0]["full_name"])
