import requests

MEDIUM_USER_ID = "1a1601223250c120b3b37426db9cd5b205566c7aec9beae73840a7f73d51e7267" 
MEDIUM_API_URL = f"https://api.medium.com/v1/users/{MEDIUM_USER_ID}/posts"
MEDIUM_TOKEN = "2b81cb0a6ee412cfa277bff8e02e80cba7ddd5d0ee662758d8df3e33254dff19c"
TITLE = "Gaia dataset and queries with ADQL (Astronomical Data Query Language)"
FILE_NAME = "ADQL.md"

def main():
    headers = {
        "Authorization": f"Bearer {MEDIUM_TOKEN}",
        "Content-Type": "application/json",
        "Accept": "application/json",
        "Accept-Charset": "utf-8"
    }

    with open(FILE_NAME, "r", encoding="utf-8") as file:
        content = file.read()

    data = {
        "title": TITLE,
        "contentFormat": "markdown",
        "content": content
    }

    response = requests.post(MEDIUM_API_URL, headers=headers, json=data)

    if response.status_code == 201:
        print("Article published successfully!")
    else:
        print(f"Error: {response.status_code}")
        try:
            error_response = response
            print(f"Error content: {error_response}")
        except ValueError:
            print("Error content is not in JSON format")

if __name__ == "__main__":
    main()