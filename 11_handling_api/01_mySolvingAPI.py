import requests

def fetch_username():
    url = "https://api.freeapi.app/api/v1/seed/generated-credentials"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        user_role = user_data[7]["role"]
        user_name = user_data[33]["username"]
        return user_role, user_name
    else:
        raise Exception("Failed to fetch the user data")
    
def main():
    try:
        role, username = fetch_username()
        print(f"Role: {role} \nUsername: {username}")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()

