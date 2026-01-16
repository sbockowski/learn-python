
def test_api_get(playwright):
    request = playwright.request.new_context(
        extra_http_headers={
            "Accept": "application/json",
            "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        }
    )
    response = request.get("https://reqres.in/api/users?page=2")
    
    # request = playwright.request.new_context()
    # response = request.get("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status == 200
    json_data = response.json()
    print(json_data)
    assert json_data["id"] == 1
    
    request.dispose()
    print("Test completed successfully.")