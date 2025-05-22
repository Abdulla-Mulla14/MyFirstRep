# iss file mein code sahi hai file get karne ke liye ya read karne ke liye par dik'kat url ke saath hai 

import requests

def user_description_details():
    url = "https://api.freeapi.app/api/v1/social-media/profile/u/rosanna_krajcik51"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        user_id = user_data["account"]["_id"]
        user_url = user_data["coverImage"]["_id"]
        return user_id, user_url
    else:
        raise Exception("Failed to fetch user data")
    
def main():
    try:
        id_s, url = user_description_details()
        print(f"Id: {id_s} \nUrl: {url}")
    except Exception as e:
        print((e))

if __name__ == "__main__":
    main()